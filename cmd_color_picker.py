#coding:utf-8
import ctypes,sys
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_color(color, handle=std_out_handle):
    succeed = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return succeed

def resetColor():
    set_cmd_color(0x0f)

def log(msg, color=0x0f, suffix='\n'):
    set_cmd_color(color)
    sys.stdout.write(msg+suffix)
    resetColor()

# Windows CMD命令行 字体颜色定义 text colors
class ForeGroundColor(object):
	BLACK = 0x00 # black.
	DARKBLUE = 0x01 # dark blue.
	DARKGREEN = 0x02 # dark green.
	DARKSKYBLUE = 0x03 # dark skyblue.
	DARKRED = 0x04 # dark red.
	DARKPINK = 0x05 # dark pink.
	DARKYELLOW = 0x06 # dark yellow.
	DARKWHITE = 0x07 # dark white.
	DARKGRAY = 0x08 # dark gray.
	BLUE = 0x09 # blue.
	PURPLE = 0x0a # purple.
	SKYBLUE = 0x0b # skyblue.
	RED = 0x0c # red.
	PINK = 0x0d # pink.
	YELLOW = 0x0e # yellow.
	WHITE = 0x0f # white.

foreGroundColor = ForeGroundColor()
 
# Windows CMD命令行 背景颜色定义 background colors
class BackGroundColor(object):
	BLUE = 0x10 # dark blue.
	GREEN = 0x20 # dark green.
	DARKSKYBLUE = 0x30 # dark skyblue.
	DARKRED = 0x40 # dark red.
	DARKPINK = 0x50 # dark pink.
	DARKYELLOW = 0x60 # dark yellow.
	DARKWHITE = 0x70 # dark white.
	DARKGRAY = 0x80 # dark gray.
	BLUE = 0x90 # blue.
	GREEN = 0xa0 # green.
	SKYBLUE = 0xb0 # skyblue.
	RED = 0xc0 # red.
	PINK = 0xd0 # pink.
	YELLOW = 0xe0 # yellow.
	WHITE = 0xf0 # white.

backgroundColor = BackGroundColor()