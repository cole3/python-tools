#!/usr/bin/env python
#coding=utf-8

import urllib, sys, re, os

base_url = "http://devimages.apple.com/iphone/samples/bipbop/"
main_m3u8 = "bipbopall.m3u8"


ext_x_targetduration = '#EXT-X-TARGETDURATION'
ext_x_media_sequence = '#EXT-X-MEDIA-SEQUENCE'
ext_x_program_date_time = '#EXT-X-PROGRAM-DATE-TIME'
ext_x_media = '#EXT-X-MEDIA'
ext_x_playlist_type = '#EXT-X-PLAYLIST-TYPE'
ext_x_key = '#EXT-X-KEY'
ext_x_stream_inf = '#EXT-X-STREAM-INF'
ext_x_version = '#EXT-X-VERSION'
ext_x_allow_cache = '#EXT-X-ALLOW-CACHE'
ext_x_endlist = '#EXT-X-ENDLIST'
extinf = '#EXTINF'
ext_i_frames_only = '#EXT-X-I-FRAMES-ONLY'
ext_x_i_frame_stream_inf = '#EXT-X-I-FRAME-STREAM-INF'
ext_x_discontinuity = '#EXT-X-DISCONTINUITY'


def parse_m3u8(url):
    list = []
    state = {
        'expect_segment': False,
        'expect_playlist': False,
        }
    content = download_content(url)
    for line in content.strip().replace('\r\n', '\n').split('\n'):
        print line
        if state['expect_playlist']:
            entend_url = line
            list.append(base_url + entend_url);
            state['expect_playlist'] = False
        elif state['expect_segment']:
            segment_name = line
            cur_base_url = (url).rsplit('/', 1)[0]
            list.append(cur_base_url + '/' + segment_name);
            state['expect_segment'] = False
        elif line.startswith(ext_x_stream_inf):
            program_id = re.search('PROGRAM-ID=(\d+)', line).group(1)
            bandwidth = re.search('BANDWIDTH=(\d+)', line).group(1)
            print ext_x_targetduration + " program_id: " + program_id + " bandwidth: " + bandwidth
            state['expect_playlist'] = True
        elif line.startswith(ext_x_targetduration):
            target_duration = re.search(ext_x_targetduration + ':(\d*?)', line).group(1)
            print "target duration: " + target_duration
        elif line.startswith(ext_x_media_sequence):
            media_sequence = re.search(ext_x_media_sequence + ':(\d*?)', line).group(1)
            print "media sequence: " + media_sequence
        elif line.startswith(extinf):
            duration = re.search(extinf + ':(\d+)', line).group(1)
            title = re.search(', (.*)', line).group(1)
            print "segmentt duration: " + duration + " title: " + title
            state['expect_segment'] = True
        elif line.startswith(ext_x_endlist):
            print "endlist"
    return list


def download_content(url):
	page = urllib.urlopen(url)
	content = page.read()
	return content

def is_playlist(url):
	return url.endswith("m3u8")

def print_list(list):
	print "-----------------------------------------------"
	for i in list:
		print i

url = base_url + main_m3u8

list = parse_m3u8(url)
print_list(list)

ts_list = parse_m3u8(list[3])

f = open('test.ts','w')
for i in ts_list:
	#os.system("ffplay -autoexit " + i)
	print i
	data = download_content(i)
	f.write(data)
f.close()

'''
for i in list:
	print i
	if is_playlist(i):
		content = download_content(i)
		l = parse_m3u8(content)
		print_list(l)
'''
