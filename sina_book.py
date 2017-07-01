# coding:utf-8
# ------------------------------------------------------------
# 简介 : 在新浪读书频道下载小说，并整理、合成为纯文本格式。方便阅读。
# ------------------------------------------------------------
# 说明 : Python 用来写一些类似的 bot 很方便，关键在于：
#       1. 网络地址的分析，从页面中分析出各个页面的 url
#       2. 读取各 url 分析你所要的内容。
#       3. 现在虽然有 BeautifulSoup 等优秀的分析模块，但是我还是很喜欢
#           用正则表达式，原因是无需第三方模块，而且正则表达式是非常有
#           用的工具，正好练习练习。
# ------------------------------------------------------------
#       这个代码当时是在 csdn 看到的。是哪位兄弟写的当时没有保留，但是就是
#       这个程序让我见识到了 python 的简洁和高效，也从学习这个程序开始接触
#       python ，并写了一些自己用的小 bot ，再次感谢哪位兄弟。
# ------------------------------------------------------------

import sys
import re
import urllib

def extract_links(html):
	html = unicode(html, 'gb2312','ignore').encode('utf-8','ignore')
	links = []
	links = re.findall(r'<a href="(chapter_[^<>]*?)"[^<>]*?>(.*?)</a>', html)
	return links

def extract_content(html):
	#html = unicode(html, 'gb2312','ignore').encode('utf-8','ignore')
	m = re.search('<div id="contTxt"[^<>]*?>(.*?)</div>', html, re.S)
	return m and html_to_text(m.group()) or ''

def html_to_text(html):
	html = re.sub(r'<p>(.*?)</p>', r'\1\n', html)
	html = re.sub(r'<[^<>]*>', '', html)
	return "\n\n" + html.strip() + "\n\n"

def url_get(url):
    u = urllib.urlopen(url)
    c = u.read()
    u.close()
    return c

def download_book(urlindex, folder):
	links = extract_links(url_get(urlindex))
	n = 0
	for link in links:
		u = 'http://vip.book.sina.com.cn/book/' + link[0]
		s = '%0.3u' % n
		filename = s + '.txt'
		fp = open(folder + '/' + filename, 'w')
		fp.write(extract_content(url_get(u)))
		fp.close()
		print u
		print filename
		n += 1

if len(sys.argv) < 3:
	print '%s [html] [folder]' % sys.argv[0]
else:
	download_book(sys.argv[1], sys.argv[2])

#《厚黑学》http://vip.book.sina.com.cn/book/index_162625.html

