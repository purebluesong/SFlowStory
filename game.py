import sys,os
sys.path.append("../")#make import the branch possible
import engine
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
	return int(input('Please choose your story'))


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

#main
def main():
	chapter = 'start' # define start chapter
	print 'start game:'
	story = engine.startStory()# choose story
	print 'OK Come on!'
	while(chapter is not 'end'):# loop the story line
		show_chapter(story[chapter][0])
		chapter = engine.getnextchapter(chapter, story)#^-^
	show_chapter(story['end'][0])

if __name__ == '__main__':
	main()
