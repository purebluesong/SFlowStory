#coding:utf-8
# this is a simple game  e... or a story teller
version = '0.16'
qq_group_num = '296386547'
initmsg = u'Game init... \nVersion:'+version+'\nCreated by HIT.SF\nAll Copyrights Reserved\nWelcome to join us !QQ group:'+qq_group_num
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
from catstory_story import variables
import game	

def make_error(msg):
    print msg

def startStory():
    choosen_story = storys[storys.keys()[game.choose_story(storys)-1]]
    return choosen_story

def isMethod(obj):
    return obj.hasattr(obj, '__call__')

def getOptions(chapter,story):
    options = []
    if type(story[chapter][1]) is not list:
        make_error('the type of the options is not list')
        return []
    for option in story[chapter][1]:
        if type(option) == tuple:
            options += [option[0]]
        elif type(option) == str or type(option) == unicode:
            options += [option]
        else:
            print type(option)
            make_error('invalid data format.\nit should be a tuple or string\nPlease contact Sprout')
    return options

def getnextchapter(chapter='start',story=storys):
    options = []
    if len(story[chapter]) == 2:
        options = getOptions(chapter,story)
    if len(story[chapter]) == 3:
        if isMethod(story[chapter][2]):
            story[chapter][2]()
        else:
            variables[chapter] = story[chapter][2]
    options += ['end']
    choose = game.choose_chapter(options)-1
    indecies = (story[chapter][1] if len(story[chapter]) > 1 else []) + ['end']
    nextchapter = indecies[choose]
    if type(nextchapter) == tuple:
        nextchapter = nextchapter[1]
    return nextchapter

print 'engine init over'

