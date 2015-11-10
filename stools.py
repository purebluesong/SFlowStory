

def intelligence_int(param, start=-1000000, end=1000000):
	if not param.isdigit():
		return None
	else:
		param = int(param)
		if param < start or param > end:
			return None
		return param