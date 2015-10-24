import sys,os
sys.path.append("../")#make import the branch possible
from multibranch_storys import *;

def input():
	raw_input(msg)

def output():
	log(msg,color,suffix)

#main
chapter = 'start' # define start chapter
story = startStory()# choose story
while(chapter is not 'end'):# loop the story line
	chapter = getnextchapter(chapter,story)#^-^

