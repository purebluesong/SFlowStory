#coding:utf-8
import sys,os
sys.path.append("../")#make import the branch possible
import engine
import stools
from cmd_color_picker import *
helpinfo = u'''帮助信息：
输入S保存进度
输入L载入进度
'''
stop_visit_story = False
branch_main = True
endFlag = 'end'
startFlag = 'start'

def input(msg):
	value = raw_input(msg)
	return value

def output(msg, color=0x0f, suffix='\n'):
	log(msg, color, suffix)

def save():
	engine.save()

def load():
	output('This is saves:', foreGroundColor.DARKSKYBLUE)
	saves = engine.get_saves()
	for save in saves:
		output(str(save[0]), foreGroundColor.PINK, ' ')
		output(save[1], foreGroundColor.PURPLE, ' ')
		output(save[2], foreGroundColor.YELLOW)
	i = int(input('choose your save'))
	return engine.load(i-1)

def inputMsgDispatch(value):
	if value in ['S', 's']:
		save()
		output('Save succeed!',foreGroundColor.YELLOW)
	elif value in ['L', 'l']:
		chapter = load()
		show_chapter(engine.getChapterContent(chapter))
		show_options(engine.getNextChapters(chapter))
	elif value in ['help', 'H', 'h']:
		output(helpinfo)
	else:
		return stools.intelligence_int(value)

def choose_story(storys):
	i = 0
	output('this is storys:')
	for story in storys:
		i += 1
		output(str(i)+story, foreGroundColor.SKYBLUE)
	story_index = inputMsgDispatch(input('Please choose your story:'))
	while not story_index:
		story_index = inputMsgDispatch(input('Please choose your story:'))
	story_index = 0 if story_index < 0 else story_index % len(storys)
	if not story_index:
		return
	print 'OK Come on!'
	return engine.chooseStory(storys[story_index-1])

def choose_chapter(chapters):
	i = 0
	output('so what will happen?', foreGroundColor.SKYBLUE, '---')
	for nextbranch in chapters:
		i += 1
		output(str(i), foreGroundColor.DARKRED, ':')
		output(nextbranch, foreGroundColor.YELLOW, ' ')
	print ' '
	return input('Please choose it!')

def show_chapter(chapter):
	output(chapter, foreGroundColor.PURPLE)

def show_options(options):
	i = 0
	for option in options:
		i += 1
		output(str(i)+' ', foreGroundColor.RED, '')
		output(option, foreGroundColor.PURPLE, '\n')


def visit_story(story):
	chapter = startFlag
	engine.resetCurrentChapter()
	while(chapter is not endFlag):# loop the story line
		show_chapter(engine.getChapterContent(chapter))
		show_options(engine.getNextChapters(chapter))
		choose = inputMsgDispatch(input('So, what is your choose'))
		while not choose:
			choose = inputMsgDispatch(input('So, what is your choose'))
		chapter = engine.chooseChapter(choose-1)
	show_chapter(engine.getChapterContent(endFlag))
	
#main
def main():
	storys = engine.getStoryList()
	story = True
	print 'start game: input \'help\' get help infomation'
	while story:
		story = choose_story(storys)
		if not story:
			break
		visit_story(story)

if __name__ == '__main__':
	main()
