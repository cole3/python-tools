#!/usr/bin/env python
#coding=utf-8


import urllib, sys, os, re

pre_url = 

for i in range(0, 163):
	url = pre_url + str(i)
	print url
	html = urllib.urlopen(url)
	ret = re.match(ur"\u6E38\u620F",html)
	print ret



