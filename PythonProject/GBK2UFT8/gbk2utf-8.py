#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import codecs
import os
import shutil
import re
import click
import chardet

version = "1.0.0"

# 清除备份文件
def clear_bak_files(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.lower().endswith('.bak'):       # 删除后缀名为bak文件
                target = os.path.join(root, file)
                print "delete--> "+target
                os.remove(target)


# 恢复备份文件
def restore_bak_files(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.lower().endswith('.bak'):
                name, suffix = os.path.splitext(file)
                source = os.path.join(root, file)   # 备份文件
                target = os.path.join(root, name)   # 目标文件
                print "restore--> "+target
                os.remove(target)                   # 删除目标源文件
                shutil.copyfile(source, target)     # 用备份文件覆盖掉目标文件

                
# 转换编码核心
def convert_encoding_core(filename, target_encoding, bak):
    # 备份文件
    if bak:
        shutil.copyfile(filename, filename + '.bak')

    # 转换编码
    content = codecs.open(filename, 'r').read()
    source_encoding = chardet.detect(content)['encoding']
    print "convert-"+target_encoding+"-> "+filename
    content = content.decode(source_encoding, 'ignore') #.encode(source_encoding)
    codecs.open(filename, 'w', encoding=target_encoding).write(content)

# 转换编码
def convert_encoding(dir, target_encoding, bak):
    for root, dirs, files in os.walk(dir):
        for f in files:
            fl = f.lower()
            if fl.endswith('.java') or fl.endswith('.cpp') or fl.endswith('.c') or fl.endswith('.h') or fl.endswith('.md') or fl.endswith('.txt'):
                filename = os.path.join(root, f)
                try:
                    convert_encoding_core(filename, target_encoding, bak)
                except Exception, e:
                    print "exception-->"
                    print filename


@click.command()
@click.option('-f', "--file",    type=str,  default=None,  help="需要编码的单个文件")
@click.option('-d', "--dir",     type=str,  default=None,  help="需要转换编码的文件夹")
@click.option('-b', "--bak",     type=bool, default=True,  help="是否生成备份文件")
@click.option('-r', "--restore", type=bool, default=False, help="恢复备份文件")
@click.option('-c', "--clear",   type=bool, default=False, help="删除备份文件")
def run(file, dir, bak, restore, clear):
    print ("---------------------------------")
    print ("GcsSloop Gbk2Utf-8 V%s" %(version))
    print ("---------------------------------")
    print ("\n")

    # 恢复备份文件
    if restore:
        if dir is not None:
            restore_bak_files(dir)
        else:
            restore_bak_files(os.getcwd())
        print "\n"
        return

    # 删除备份文件
    if clear:
        if dir is not None:
            clear_bak_files(dir)
        else:
            clear_bak_files(os.getcwd())
        print "\n"
        return

    # 转换编码
    if file is not None:
        convert_encoding_core(file, 'utf-8', bak)
    elif dir is not None:
        convert_encoding(dir, 'utf-8', bak)
    else:
        convert_encoding(os.getcwd(), 'utf-8', bak)
    print "\n"


if __name__ == '__main__':
    run()

