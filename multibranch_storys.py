#coding:utf-8
# this is a simple game  e... or a story teller
version = '0.13'
qq_group_num = '296386547'
initmsg = u'game init... \nversion:'+version+'\ncreate by HIT.SF\nAll copyrights reserved\nWelcome to join us !QQ group:'+qq_group_num
print initmsg
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
from catstory_story import storys
from cmd_color_picker import *

def input(msg):
	return raw_input(msg)

def output(msg,color=0x0f,suffix='\n'):
	log(msg,color,suffix)

def startStory():
	output('Please choose story',foreGroundColor.PURPLE)
	i=0
	for story in storys:
		i+=1
		output(str(i)+' '+story,foreGroundColor.SKYBLUE)

	choose = int(input('Please choose your story'))
	choosen_story = storys[storys.keys()[choose-1]]
	output('\nStart story now!\n',foreGroundColor.PINK)
	return choosen_story

def getnextchapter(chapter,story):
	nextchapter = None
	output(story[chapter][0],foreGroundColor.PURPLE)
	output('so what will happen?',foreGroundColor.SKYBLUE,'---')
	i=0
	for nextbranch in story[chapter][1:]:
		i+=1
		output(str(i),foreGroundColor.DARKRED,':')
		output(nextbranch,foreGroundColor.YELLOW,' ')
	print ' '
	nextchapter = story[chapter][int(input('Please choose it!'))]
	return nextchapter

#chapter = 'start'
#while(chapter is not 'end'):
#	chapter = getnextchapter(chapter)

