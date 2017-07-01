#!/usr/bin/env python
#coding=utf-8

import urllib, sys, os, re


base_url = 'http://www.xxxx.com'
sub_url = '/xxxx/xxxx/index.html'


main_url = base_url + sub_url
print main_url

main_html = urllib.urlopen(main_url)
main_text = main_html.read()#.decode('GB2312')

pattern = 'class="zxsyt".*href="(.*?)"'
addrs = re.findall(pattern, main_text)
	
pattern = 'class="zxsyt".*title="(.*?)"'
titles = re.findall(pattern, main_text)

for i in range(0, len(addrs)):
	name = re.match(ur"[\u4e00-\u9fa5]*", titles[i].decode('utf8'))

	page_url = base_url + addrs[i]
	page_html = urllib.urlopen(page_url)
	page_text = page_html.read()

	pattern = '<img src="(.*?)" border'
	pic_urls = re.findall(pattern, page_text)

	print page_url
	num = 0

	for pic_url in pic_urls:
		pic_html = urllib.urlopen(pic_url)
		pic_data = pic_html.read()
		file = open(name.group(0) + "%03d" % num + ".jpg", 'ab')
		file.write(pic_data)
		file.close()
		num += 1
		print '#',
	print ''
