#coding:utf-8

import sys
import re
import urllib


# http://yl.cnreaders.com/2015_04/yili20150401.html
year = 2015
month = 4


def mk_url(year, month, num):
	url = 'http://yl.cnreaders.com/%d_%02d/yili%d%02d%02d.html' % (year, month, year, month, num)
	return url

def get_content(url):
    u = urllib.urlopen(url)
    content = u.read()
    u.close()
    return content

def get_title(content):
	content = content.decode('utf-8')
	title = re.findall(r'<h1>(.*?)</h1>', content)
	return title

def get_text(content):
	text = re.findall(r'<p>(.*?)[\n,<]', content)
	return text


if len(sys.argv) < 3:
	print '%s [year] [month]' % sys.argv[0]
	exit()

year = int(sys.argv[1])
month = int(sys.argv[2])
num = 1

while True:
	url = mk_url(year, month, num)
	content = get_content(url)
	title = get_title(content)
	text = get_text(content)
	print title
	if title[0] == 'Not Found':
		break
	fp = open(title[0] + '.txt', 'w')
	for t in text:
		fp.write(t+'\n')
	fp.close()
	num += 1

print 'get done.'