#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import os.path
import click
import tinify
import platform

tinify.key = "在此处填写你申请的API"		# API KEY
version = "1.1.0"		# 版本号
voice = True			# 是否语音提示

def say(content):
	if platform.system() == "Darwin" and voice == True:
		print content
		os.system("say '"+content+"' ")
	else:
		print content
	pass

# 压缩的核心
def compress_core(inputFile, outputFile, img_width):
	source = tinify.from_file(inputFile)
	if img_width is not -1:
		resized = source.resize(method = "scale", width  = img_width)
		resized.to_file(outputFile)
	else:
		source.to_file(outputFile)

# 压缩一个文件夹下的图片
def compress_path(path, width):
#	print "压缩指定目录下文件!"
	if not os.path.isdir(path):
		say("骗纸! 这根本不是一个文件夹!")
		return
	else:
		say("尝试压缩, 请稍后!")
		fromFilePath = path 			# 源路径
		toFilePath = path+"/tiny" 		# 输出路径
#		print "fromFilePath=%s" %fromFilePath
#		print "toFilePath=%s" %toFilePath
		for root, dirs, files in os.walk(fromFilePath):
			print "root = %s" %root
			print "dirs = %s" %dirs
			print "files= %s" %files
			for name in files:
				fileName, fileSuffix = os.path.splitext(name)
				if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
					toFullPath = toFilePath + root[len(fromFilePath):]
					toFullName = toFullPath + '/' + name
					if os.path.isdir(toFullPath):
						pass
					else:
						os.mkdir(toFullPath)
					compress_core(root + '/' + name, toFullName, width)
			break									# 仅遍历当前目录

# 仅压缩指定文件
def compress_file(inputFile, width):
#	print "压缩指定文件!"
	if not os.path.isfile(inputFile):
		say("骗纸! 这根本不是文件!")
		return
	say("尝试压缩, 请稍后!")
#	print "file = %s" %inputFile
	dirname  = os.path.dirname(inputFile)
	basename = os.path.basename(inputFile)
	fileName, fileSuffix = os.path.splitext(basename)
	if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
		compress_core(inputFile, dirname+"/tiny_"+basename, width)
	else:
		say("不支持该文件类型!")

@click.command()
@click.option('-f', "--file",  type=str,  default=None,  help="单个文件压缩")
@click.option('-d', "--dir",   type=str,  default=None,  help="被压缩的文件夹")
@click.option('-w', "--width", type=int,  default=-1,    help="图片宽度，默认不变")
def run(file, dir, width):
	print ("GcsSloop TinyPng V%s" %(version))
	say("启动压缩魔法!")
	if file is not None:
#		say("压缩指定文件!")
		compress_file(file, width)				# 仅压缩一个文件
		pass
	elif dir is not None:
#		say("压缩指定目录下所有图片文件")
		compress_path(dir, width)				# 压缩指定目录下的文件
		pass
	else:
#		say("压缩当前目录下所有图片文件")
		compress_path(os.getcwd(), width)		# 压缩当前目录下的文件
	say("魔法结束!")

if __name__ == "__main__":
    run()
