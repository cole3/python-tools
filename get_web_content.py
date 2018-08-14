#coding:utf-8

import sys, os
import re
import urllib2


url = 'http://www.physicsandmathstutor.com/past-papers/a-level-chemistry/aqa-unit-6/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

def get_content(url):
    req = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

def get_addrs(content):
    content = content.decode('utf-8')
    addrs = re.findall(r'(http://.*?\.pdf)', content)
    return addrs

def save_files(addrs):
    for addr in addrs:
        name = os.path.basename(addr)
        print "Downloading: " + name
        fp = open(name, 'w')
        content = get_content(addr)
        fp.write(content)
        fp.close()

content = get_content(url)
#print content
addrs = get_addrs(content)
#print addrs
save_files(addrs)
print 'Done.'
