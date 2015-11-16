import time

def intelligence_int(param, start=-1000000, end=1000000):
	if not param.isdigit():
		return None
	else:
		param = int(param)
		if param < start or param > end:
			return None
		return param

def getNowTime_Int():
	return int(time.mktime(time.localtime()))

def getNowTime_Str(timestramp=None):
	if timestramp:
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestramp))
	else :
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())