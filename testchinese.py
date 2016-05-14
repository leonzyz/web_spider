#!/usr/bin/python
#-*- coding:utf-8 -*-

haha=r'哈哈'
print haha

print "hello"
__author__= "leonzyz"
import os
import re
fin=open('webpage.txt','r')

page=fin.read()
#line=fin.readline()
pattern=re.compile(r'<div class="topic-content">.*?<div',re.S)
#pattern=re.compile(r'<div>.*</div>')
match=pattern.search(page)

subline=match.group()
chinese=u'【多肉】'
print chinese
#pattern2=re.compile(r'【多肉】.*?（图）')
#match=pattern.search(subline)
#if match:
#	print match.group()
#
#fin.close()
fin.close()



