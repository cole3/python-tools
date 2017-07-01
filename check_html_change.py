#!/usr/bin/env python
import urllib
import time, re
import win_notify

html = "http://nicej.taobao.com/view_page-639877483.htm"

f = urllib.urlopen(html)
old = f.read()
f.close()

url = re.findall('<area href="(.*?)"', old)
pre = len(url)
#print url
print "cur url num is %d   " % pre,
print "time:" + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
win_notify.MainWindow(" ", "start to check...", 3)

while True:
	time.sleep(10)
	f = urllib.urlopen(html)
	new = f.read()
	f.close()
	url = re.findall('<area href="(.*?)"', new)
	cur = len(url)
	if pre != cur:
		print "cur url num is %d   " % cur
		print "time:" + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
		pre = cur;
		print "Got it change! time:" +  time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
		win_notify.MainWindow(" ", "Html change!", 10000)
