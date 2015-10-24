#coding:utf-8
# this is a simple game  e... or a story teller
version = '0.14'
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

def choose_story(storys):
	output('Please choose story',foreGroundColor.PURPLE)
	i=0
	for story in storys:
		i+=1
		output(str(i)+' '+story,foreGroundColor.SKYBLUE)
	output('\nYou have choosen a story!\n',foreGroundColor.PINK)
	return int(input('Please choose your story'))
	
def startStory():
	choosen_story = storys[storys.keys()[choose_story()-1]]
	return choosen_story

def choose_chapter(chapters):
	i=0
	output('so what will happen?',foreGroundColor.SKYBLUE,'---')
	for nextbranch in chapters:
		i+=1
		output(str(i),foreGroundColor.DARKRED,':')
		output(nextbranch,foreGroundColor.YELLOW,' ') 
	print ' '
	return int(input('Please choose it!'))

def show_chapter(chapter):
	output(chapter,foreGroundColor.PURPLE)

def getnextchapter(chapter,story):
	show_chapter(story[chapter][0])
	nextchapter = story[chapter][choose_chapter(story[chapter][1:])]
	return nextchapter

#chapter = 'start'
#while(chapter is not 'end'):
#	chapter = getnextchapter(chapter)

