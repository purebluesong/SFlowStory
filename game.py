import sys,os
sys.path.append("../")#make import the branch possible
import engine
from cmd_color_picker import *
helpinfo = u'''帮助信息：
输入S保存进度
输入L载入进度
'''
stop_loop_chapter = False

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
		output(str(save[0]), foreGroundColor.PINK,' ')
		output(save[1], foreGroundColor.PURPLE, ' ')
		output(save[2], foreGroundColor.YELLOW)
	i = int(input('choose your save'))
	engine.load(i-1)

def inputMsgDispatch(value):
	if value == 'S':
		save()
	elif value == 'L':
		load()
	elif value == 'help':
		output(helpinfo)
	else:
		try:
			value = int(value)
		except Exception, e:
			value = None
			raise e
		else:
			return value		

def choose_story(storys):
	output('Stories', foreGroundColor.PURPLE)
	i = 0
	for story in storys:
		i += 1
		output(str(i)+' '+story, foreGroundColor.SKYBLUE)
	return input('Please choose your story')

def choose_chapter(chapters):
	i=0
	output('so what will happen?',foreGroundColor.SKYBLUE,'---')
	for nextbranch in chapters:
		i+=1
		output(str(i),foreGroundColor.DARKRED,':')
		output(nextbranch,foreGroundColor.YELLOW,' ') 
	print ' '
	return input('Please choose it!')

def show_chapter(chapter):
	output(chapter,foreGroundColor.PURPLE)

def loop_chapter(chapter):
	while(chapter is not 'end' && !stop_loop_chapter):# loop the story line
		show_chapter(story[chapter][0])
		chapter = engine.getnextchapter(chapter, story)#^-^
	
#main
def main():
	chapter = 'start' # define start chapter
	print 'start game: input \'help\' get help infomation'
	story = engine.startStory()# choose story
	print 'OK Come on!'
	loop_chapter(chapter)
	show_chapter(story['end'][0])

if __name__ == '__main__':
	main()
