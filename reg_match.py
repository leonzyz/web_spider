#!/usr/bin/python
#-*- coding:utf-8 -*-

print "hello"
__author__= "leonzyz"
import os
import re
import shutil
import urllib
fin=open('webpage.txt','r')
working_dir=os.path.abspath('.')
download_dir=os.path.join(working_dir,'download')
if os.path.exists(download_dir):
	shutil.rmtree(download_dir)
	#os.rmdir(download_dir)
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
name_dict={}
if match:
	for m in match:
		name=m[0]
		url=m[1]
		parent_name,sub_name=name.split(' ',1)
		#print "name=%s \t url=%s" % (name,url)
		#print "parent name=%s \t sub name=%s" % (parent_name,sub_name)
		if name_dict.has_key(parent_name):
			if name_dict[parent_name].has_key(sub_name):
				break
			else:
				sub_name_path=os.path.join(download_dir,parent_name,sub_name)
				name_dict[parent_name][sub_name]=(sub_name_path,url)
				os.mkdir(sub_name_path)
				print "mkdir %s" % sub_name_path
		else:
			parent_name_path=os.path.join(download_dir,parent_name)
			os.mkdir(parent_name_path)
			print "mkdir %s" % parent_name_path
			sub_name_path=os.path.join(download_dir,parent_name,sub_name)
			name_dict[parent_name]={sub_name:(sub_name_path,url)}
			os.mkdir(sub_name_path)
			print "mkdir %s" % sub_name_path
#print name_dict
#
#fin.close()
fin.close()

for parent_name in name_dict:
	for sub_name in name_dict[parent_name]:
		print "path:%s \t url:%s" % name_dict[parent_name][sub_name]
		path,url=name_dict[parent_name][sub_name]
		f=urllib.urlopen(url)
		page=f.read()
		fout=open(os.path.join(path,sub_name),'w')
		fout.write(page)
		fout.close()



