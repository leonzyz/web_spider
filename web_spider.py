#!/usr/bin/python

print "hello"
__author__= "leonzyz"


import urllib
import os
import re
f=urllib.urlopen('https://www.douban.com/group/topic/40100855/')
page=f.read()
#print page
#pattern=re.compile(r'<div class="topic-content">.*</div>',re.D)
pattern=re.compile(r'<div>.*</div>')
match=pattern.match(page)
if match:
	print match.group()




