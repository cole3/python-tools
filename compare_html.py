import urllib
import time

html = "http://nicej.taobao.com/view_page-639877483.htm?spm=a1z10.1.7272581-609321757.1.QU1Ntj"

f = urllib.urlopen(html)
old = f.read()
f.close()

while True:
	time.sleep(1)
	f = urllib.urlopen(html)
	new = f.read()
	f.close()
	if new != old:
		old = new;
		print "Got it change!"