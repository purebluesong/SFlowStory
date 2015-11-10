#coding:utf-8
# this is a simple game  e... or a story teller
version = '0.16'
qq_group_num = '296386547'
initmsg = u'Game init... \nVersion:'+version+'\nCreated by HIT.SF\nAll Copyrights Reserved\nWelcome to join us !QQ group:'+qq_group_num
print initmsg
import sys, os
import time
from catstory_story import storys
from catstory_story import variables
current_chapter = 'start'
save_suffix = '.hit.sf'
split_symbol = '$$$'
choosen_story = storys.get(storys.keys()[0])

def make_error(msg):
    print msg

def getStoryList():
    return storys.keys()

def chooseStory(story_name):
    global choosen_story
    choosen_story = storys[story_name]
    return choosen_story
 
def isMethod(obj):
    return obj.hasattr(obj, '__call__')

def getOptions(chapter, story):
    options = []
    secondOption = story[chapter][1]
    if type(secondOption) is not list:
        make_error('the type of the options is not list')
        return []
    for option in secondOption:
        if type(option) == tuple:
            options += [option[0]]
        elif type(option) == str or type(option) == unicode:
            options += [option]
        else:
            print type(option)
            make_error('invalid data format.\nit should be a tuple or string\nPlease contact Sprout')
    return options

def save(name='default', timestramp=True):
    global current_chapter
    try:
        f = open(name + save_suffix, 'a+')
        f.write(current_chapter+(split_symbol+str(int(time.mktime(time.localtime())))) if timestramp else '')
        f.close()
    except Exception, e:
        raise
        return True
    else:
        return False

def get_saves(name='default'):
    saves = []
    i = 0
    try:
        f = open(name+save_suffix, 'r')
        records = str(f.read()).split('\n')
        f.close()
        for record in records:
            record = record.split(split_symbol)
            if len(record) > 1:
                timestramp = int(record[1])
                record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestramp))
                saves.append((i, record[0], record_time))
            else:
                saves.append((i, record))
            i += 1
    except Exception, e:
        make_error('error:Maybe the file does not exit')
        raise e
        return saves
    else:
        return saves

def load(version=-1, name='default'):
    global current_chapter
    try:
        f = open(name+save_suffix, 'r')
        records = str(f.read()).split('\n')
        if version == -1 or version > len(records):
            current_chapter = (records[-1]).split('$$$')[0]
        if len(records) > version:
            current_chapter = (records[version]).split('$$$')[0]
        f.close()
    except Exception, e:
        make_error('error:load-Maybe file does not exist')
        raise
    return current_chapter

def getNextChapters(chapter='start'):
    options = []
    if len(choosen_story[chapter]) == 2:
        options = getOptions(chapter, choosen_story)
    if len(choosen_story[chapter]) == 3:
        if isMethod(choosen_story[chapter][2]):
            choosen_story[chapter][2]()
        else:
            variables[chapter] = choosen_story[chapter][2]
    options += ['end']
    return options

def getChapterContent(chapter='start'):
    global choosen_story
    chapter = choosen_story.get(chapter)
    if not chapter:
        make_error('could not find the chapter')
        return 'end'
    return chapter[0]

def resetCurrentChapter():
    global current_chapter
    current_chapter = 'start'

def chooseChapter(choose=-1):
    global current_chapter, choosen_story
    indecies = (choosen_story[current_chapter][1] if len(choosen_story[current_chapter]) > 1 else []) + ['end']
    nextchapter = indecies[choose]
    if type(nextchapter) == tuple:
        nextchapter = nextchapter[1]
    current_chapter = nextchapter
    return current_chapter

print 'engine init over'
