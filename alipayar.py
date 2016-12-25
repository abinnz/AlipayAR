# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
import os,sys
import configparser

# 线索图参数
config = {}

def handlerImg(path,savepath=''):

    filename=path[path.rfind('/')+1:]
    extension=path[path.rfind('.')+1:]

    #读取图像
    im = Image.open(path)
    w = im.width
    h = im.height

    global config
    pos=config.get(str(w)+'*'+str(h))
    if pos==None:
        pos=config.get('width*height')

    left=pos['left']
    top=pos['top']
    width=pos['width']
    height=pos['height']
    #从截图中裁出线索图片
    pic=im.crop((left,top,left+width,top+height))

    # 高度偏移值
    margin = config.get('margin')
    # 黑线宽度
    blanLineHeight = config.get('blanLineHeight')

    # 为了减少误差将线索图片分成两次循环
    # 1 至 14条黑线
    for index in range(0,int(config.get('blanLineSize')/2) + 1):
        if index == 0:
            copyandpaste(pic,margin[0],width,blanLineHeight)
        else:
            copyandpaste(pic,margin[0]+(margin[1]+blanLineHeight)*index,width,blanLineHeight)
    # 27 至 15条黑线
    for index in range(config.get('blanLineSize') - 1,int(config.get('blanLineSize') / 2) , -1):
    	seq = config.get('blanLineSize') - 1 - index 
    	if seq == 0:
    		copyandpaste(pic,pic.height - margin[0] - blanLineHeight,width,blanLineHeight)
    	else:
    		copyandpaste(pic,pic.height - margin[0] - blanLineHeight - (blanLineHeight + margin[1])*seq,width,blanLineHeight)
    if ''==savepath:
        pic.show()
    else:
        pic.save(savepath+'/'+filename,extension)

def copyandpaste(pic,start,width,blanLineHeight):
    halfHeight = int(blanLineHeight / 2)
    # 方法一
    # tmp=pic.crop((0,start - halfHeight,width,start))
    # pic.paste(tmp,(0,start))
    # tmp=pic.crop((0,start + blanLineHeight,width,start + blanLineHeight + halfHeight))
    # pic.paste(tmp,(0,start + halfHeight))

    # 方法二
    tmp=pic.crop((0,start - 1,width,start))
    for i in range(0,halfHeight):
    	pic.paste(tmp,(0,start+i))
    tmp=pic.crop((0,start + blanLineHeight,width,start + blanLineHeight + halfHeight))
    for i in range(0,halfHeight):
    	pic.paste(tmp,(0,start + halfHeight + i))

def input():

    if (len(sys.argv))<2:
        print('错误：请输入图片路径\npython alipayar.py [filepath]')
        return
    else:
    	if sys.argv[1] == 'png': # 新增png参数
    		for file in os.listdir("."):
    			if file.endswith('png') or file.endswith('PNG'): 
    				handlerImg(file)
    	else:
	        path1=sys.argv[1] # 原路径
	        if os.path.isdir(path1):
	            if len(sys.argv)<3:
	                print('错误：请输入两个目录\npython alipayar.py [inputpath] [outputpath]')
	                return
	            else:
	                path2=sys.argv[2] # 输入目录
	                for file in os.listdir(path1):
	                    path = os.path.join(path1, file).lower()
	                    if path.endswith('png'):
	                        handlerImg(path,path2)
	        else:
	            handlerImg(sys.argv[1])

def initConfig():
	global config
	appConfig = configparser.ConfigParser()
	appConfig.read('alipayar_config.ini',encoding='utf-8')
	phone = appConfig.get('system','phone')
	left = int(appConfig.get(phone,'left'))
	top = int(appConfig.get(phone,'top'))
	width = int(appConfig.get(phone,'width'))
	height = int(appConfig.get(phone,'height'))
	marginArray = appConfig.get(phone,'margin').split(',')
	margin = (int(marginArray[0]),int(marginArray[1]))
	blanLineHeight = int(appConfig.get(phone,'blankLineHeight'))
	blanLineSize = int(appConfig.get(phone,'blankLineSize'))
	config['width*height'] = {'left': left,'top': top,'width': width,'height': height}
	config['margin'] = margin
	config['blanLineHeight'] = blanLineHeight
	config['blanLineSize'] = blanLineSize

if __name__ == '__main__':
    initConfig()
    input()
    


    