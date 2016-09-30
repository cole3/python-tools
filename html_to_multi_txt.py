import sys
import os
import re
import urllib


help_msg = '%s [html] [txt folder]' % sys.argv[0]

def extract_links(html):
    blocks = re.findall(r'<ul class="list_009">.*?</ul>', html, re.S)
    links = []
    for b in blocks:
        links += re.findall(r'<a href="(chapter.*?)"[^<>]*>([^<>]*)</a>', b)
    return links

def extract_content(html):
    m = re.search('<div id="contTxt"[^<>]*>.*?</div>', html, re.S)
    return m and html_to_text(m.group()) or ''

def html_to_text(html):
    html = re.sub(r'<p>(.*?)</p>', r'\t\1\n', html)
    html = re.sub(r'<[^<>]*?>', r'', html)
    return "\n\n" + html.strip() + "\n\n"

def url_get(url):
    u = urllib.urlopen(url)
    c = u.read()
    u.close()
    return c

def download_book(urlindex, folder):
    links = extract_links(url_get(urlindex))

    for link in links:
		u = 'http://vip.book.sina.com.cn/book/' + link[0]
		title = link[1] + '.txt'
		filename = os.path.join(folder, title)
		fp = open(filename, 'w')
		fp.write(extract_content(url_get(u)))
		fp.close()
		print u
		print title

if len(sys.argv) < 3:
	print help_msg
else:
	if not os.path.isdir(sys.argv[2]):
		os.mkdir(sys.argv[2])
	download_book(sys.argv[1], sys.argv[2])
	