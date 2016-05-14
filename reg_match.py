#!/usr/bin/python
#-*- coding:utf-8 -*-

print "hello"
__author__= "leonzyz"
import os
import re
fin=open('webpage.txt','r')
working_dir=os.path.abspath('.')
download_dir=os.path.join(working_dir,'download')
if os.path.exists(download_dir):
	os.rmdir(download_dir)
os.mkdir(download_dir)

page=fin.read()
#line=fin.readline()
pattern=re.compile(r'<div class="topic-content">.*?<div',re.S)
#pattern=re.compile(r'<div>.*</div>')
match=pattern.search(page)

subline=match.group()
#chinese=u'【多肉】'
#print chinese
pattern2=re.compile(r'【多肉】(?P<name>.*?)（图）.*?href="(?P<url>.*?)"')
#pattern2=re.compile(r'【多肉】(?P<name>.*?)（图）');
#match=pattern2.search(subline)
match=pattern2.findall(subline)
if match:
	for m in match:
		name=m[0]
		url=m[1]
		print "name=%s \t url=%s" % (name,url)
#
#fin.close()
fin.close()



