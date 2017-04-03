#!/usr/bin/env python
#coding=utf-8

import urllib, sys, os
import re

#web address:
#http://crypto.nknu.edu.tw/AOSP/Android6/frameworks/av/media/libmediaplayerservice/
#http://androidxref.com/6.0.0_r1/raw/frameworks/av/media/libstagefright/foundation/AMessage.cpp

code_base_url = "http://androidxref.com/6.0.0_r1/"

file_pattern = '</td><td><a href=\"(.+?)\"'


def get_url_files(html_url, code_url, local_addr):
    n = 0
    index_page = urllib.urlopen(code_url)
    index_content = index_page.read()
    #print index_content
    file_names = re.fileall(file_pattern, index_content)
    print file_names
    
    for file_name in file_names:
        if file_name[-1] == '/':
            n += get_url_files(html_url+file_name, code_url+file_name, local_addr+file_name)
        else:
            print code_url + file_name
            code_page = urllib.urlopen(code_url + file_name)
            code_content = code_page.read()
            if not os.path.exists(local_addr):
                os.makedirs(local_addr)
            f = open(local_addr + file_name, 'w')
            f.write(code_content)
            f.close()
            code_page.close()
            n = n + 1
    index_page.close()
    return n

	
num = 0

if len(sys.argv) < 2:
	print "usage: " + sys.argv[0] + " [code_dir] "
	print "(for example: " + sys.argv[0] + " frameworks/av/media/libmediaplayerservice/"
	sys.exit()
	
html_url = code_base_url + "xref/" + sys.argv[1]
code_url = code_base_url + "raw/" + sys.argv[1]

print "Now, get code from: " + html_url

num = get_url_files(html_url, code_url, sys.argv[1])

print "\nGot them, total %d files" % num
