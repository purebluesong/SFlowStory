#coding:utf-8
# 书写中文内容需要在字符串前面加上表示utf8的u符号
mystory = {
	'start':['this is a long story','morning','flag2','end'],
	'morning':['In a cold morning,stranger appeared in the conner of this street','cat','end'],
	'cat':['and a cat jump out from a trash can. Strangely, this cat looks like very clean.','magic','end'],
	'magic':['"Thanks, you respect our appointment"the stanger says quitely. He sway his right hand, and the cat become a beautiful girl','end'],
	'technology':['the cat step slowly to the stranger.','end'],
	'flag2':['the story tells a boy and a girl\'s love','end'],
	'end':['all branch end']
	}

luchuan_story = {
	'start':[u'陆川在明天早上醒过来，发现他的节操和内裤都落在昨天了',u'明天','end'],
	u'明天':[u'陆川不打算扔掉节操出门，所以他决定先穿上外套去昨天找内裤和节操',u'时光鸡',u'时光机',u'更奇怪的方法','end'],
	u'时光鸡':[u'陆川纵身一跃，骑上了自家的时光鸡决定回到昨天，时光鸡开始咯咯的叫起来，两眼释放出精光','end'],
	u'时光机':[u'陆川迅速的在外套上又加了一层雨衣，冲到了放在浴室里面的热浴盆时光机','end'],
	u'更奇怪的方法':[u'陆川慢条斯理的收拾好房间，擦洗用过早点的桌子，叠整齐被子，打开阳台上的窗户，然后从窗户跳了下去','end'],
	'end':[u'真是个让人愉快的故事']
	}

storys = {'mystory':mystory,u'陆川故事':luchuan_story}
