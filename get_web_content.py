#coding:utf-8

import sys, os, time
import re
import urllib2


#url = 'http://www.physicsandmathstutor.com/a-level-maths-papers/c1-edexcel/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

only_addr = 0


def get_content(url, retries=10):
	while True:
		html = ""
		req = urllib2.Request(url, headers=hdr)
		try:
			response = urllib2.urlopen(req, timeout=20)
			html = response.read()
		except Exception, what:
			retries = retries - 1
			if retries > 0:
				print "retry"
				continue
		return html
	
def get_addrs(content):
    content = content.decode('utf-8')
    addrs = re.findall(r'(http://.*?\.pdf)', content)
    return addrs

def save_files(addrs):
	print "Downloading: pdf addresses"
	fp = open("address.txt", 'w')
	for addr in addrs:
		fp.write(addr+'\n')
	fp.close()
	
	if only_addr:
		return
	
	for addr in addrs:
		name = os.path.basename(addr)
		print "Downloading: " + name
		content = get_content(addr)
		if content:
			fp = open(name, 'wb')
			fp.write(content)
			fp.close()
		else :
			print "Download fail: " + name

			


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print '%s [web_address]' % sys.argv[0]
		print '%s --only_addr [web_address]' % sys.argv[0]
		exit()
		
	if len(sys.argv) > 2:
		if sys.argv[1] == "--only_addr":
			only_addr = 1
		
	url = sys.argv[-1]

	content = get_content(url)
	#print content
	addrs = get_addrs(content)
	#print addrs
	save_files(addrs)
	print 'Done.'
