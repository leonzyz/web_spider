#!/usr/bin/python
#-*- coding:utf-8 -*-

print "hello"
__author__= "leonzyz"


import urllib
import os
import re
import shutil

working_dir=os.path.abspath('.')
download_dir=os.path.join(working_dir,'download')
pic_dir=os.path.join(working_dir,'pic')
if os.path.exists(download_dir):
	shutil.rmtree(download_dir)

if os.path.exists(pic_dir):
	shutil.rmtree(pic_dir)
os.mkdir(download_dir)
os.mkdir(pic_dir)


f=urllib.urlopen('https://www.douban.com/group/topic/40100855/')
page=f.read()

pattern=re.compile(r'<div class="topic-content">.*?<div',re.S)
match=pattern.search(page)

subline=match.group()
pattern2=re.compile(r'【多肉】(?P<name>.*?)（图）.*?href="(?P<url>.*?)"')
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

for parent_name in name_dict:
	for sub_name in name_dict[parent_name]:
		print "path:%s \t url:%s" % name_dict[parent_name][sub_name]
		path,url=name_dict[parent_name][sub_name]
		f=urllib.urlopen(url)
		pic_pattern=re.compile(r'<div class="topic-figure cc.*?src="(?P<pic_url>.*?)" alt=.*?<div',re.S)
		page=f.read()
		match=pic_pattern.findall(page)
		if match:
			print "find a file"
			for m in match:
				pic_url=m
				print pic_url 
				url_split=pic_url.split('/')
				filename=url_split[-1]
				filepath=os.path.join(pic_dir,filename)
				urllib.urlretrieve(pic_url,filepath)
				target_path=os.path.join(path,filename)
				shutil.copy(filepath,target_path)
				







