#!/usr/bin/env python
#coding=utf-8

import urllib ,sys
import re

province_map = (["anhui", "AAH"], ["guangzhou", "AGZ"])

def show_qq_weather(qq_url):
	wetherhtml = urllib.urlopen(qq_url)
	result = wetherhtml.read().decode('GB2312')
	
	pattern = 'Title.+<b>(.+)</b>'
	Title = re.search(pattern,result).group(1)
	
	pattern = '>(\d*-\d*-\d*.+?)<'
	date = re.findall(pattern,result)
	
	pattern = 'alt="(.+?)"'
	weather = re.findall(pattern,result)
	
	pattern = '<td>([-]?\d+.*?)</td>'
	temperature = re.findall(pattern,result)
	
	print Title
	length = len(date)
	for i in range(length):
		print '\t', date[i], '\t', weather[i], '\t', temperature[i]


def show_gov_weather(gov_url):
	wetherhtml = urllib.urlopen(gov_url)
	result = wetherhtml.read().decode('utf-8')
	
	pattern = '<title>.*?</title>'
	Title = re.search(pattern,result).group(1)
	
	pattern = '>(\d*-\d*-\d*.+?)<'
	date = re.findall(pattern,result)
	
	pattern = 'alt="(.+?)"'
	weather = re.findall(pattern,result)
	
	pattern = '<td>([-]?\d+.*?)</td>'
	temperature = re.findall(pattern,result)
	
	print Title
	length = len(date)
	for i in range(length):
		print '\t', date[i], '\t', temperature[i], '\t', weather[i]


provice = raw_input('输入省名(请使用拼音 [default:anhui]):')
if len(provice) == 0:
	provice = 'anhui'
major = raw_input("输入市名(请使用拼音 [default:hefei]):")
if len(major) == 0:
	major = 'hefei'
	
	
qq_url = "http://qq.ip138.com/weather/"+provice+'/'+major+'.htm'
#print qq_url
show_qq_weather(qq_url)


for i in range(0, len(province_map)):
	if province_map[i][0] == provice:
		provice = province_map[i][1]
		break
		
#gov_url = "http://wap.weather.gov.cn/forecast/"+provice+'/'+major+'.html'
#print gov_url
#show_gov_weather(gov_url)


key = raw_input("Press enter key to exit.")