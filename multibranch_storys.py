#coding:utf-8
# this is a simple game  e... or a story teller
version = '0.12'
qq_group_num = '296386547'

print u'game init... \nversion:'+version+'\ncreate by HIT.SF\nAll copyrights reserved\nWelcome to join us !QQ group:'+qq_group_num

import sys,os
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

sys.path.append(cur_file_dir())
# import catstory_story
from catstory_story import storys
from cmd_color_picker import *

print 'Please choose story'
i=0
for story in storys:
	i+=1
	log(str(i)+' '+story,foreGroundColor.SKYBLUE)

choose = int(raw_input('Please choose your story'))
choosen_story = storys[storys.keys()[choose-1]]

log('\nStart story now!\n',foreGroundColor.PINK)
def getnextchapter(chapter):
	nextchapter = None
	log(choosen_story[chapter][0],foreGroundColor.PURPLE)
	log('so what will happen?',foreGroundColor.SKYBLUE,'---')
	i=0
	for nextbranch in choosen_story[chapter][1:]:
		i+=1
		log(str(i),foreGroundColor.DARKRED,':')
		log(nextbranch,foreGroundColor.YELLOW,' ')
	print ' '
	nextchapter = choosen_story[chapter][int(raw_input('Please choose it!'))]
	return nextchapter

chapter = 'start'
while(chapter is not 'end'):
	chapter = getnextchapter(chapter)

