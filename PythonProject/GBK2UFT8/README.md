# GBK 转 UTF-8
[![License](https://img.shields.io/badge/license-Apache%202-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
![version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)


### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

## 前言

由于之前是在 windows 平台编程，早期都是使用windows的默认编码 GBK (后期编码都换成了UTF-8)，但在 Mac 平台打开的时候不支持，显示乱码，而且在之前写的库和之后写的库混用的时候也会由于编码而出现一些莫名的问题。

出于以上原因，才有了这个编码转换脚本。

## 已有功能

功能         | 简介
-------------|--------------------------------------------------------------------
**编码识别** | 为了防止转换出错，采用编码自动识别，大部分的编码都可以自动识别转换。
**循环遍历** | 自动遍历指定文件夹下的所有文本文件(根据后缀名区分)。
**自动备份** | 默认会自动生成后缀名为 `.bak` 的备份文件，以便转换出错后恢复。
**批量恢复** | 可以批量根据备份文件恢复到之前的内容。
**参数支持** | 支持参数，更佳方便，参数详解见下文中详解

## 参数支持

参数  | 全称    | 参数类型 | 默认值 | 摘要                | 示例
-----|---------|-------- |------ |--------------------|------
无参  |         |        |       | 转换当前目录下所有文件 | `gbk2utf-8.py`
`-f` | file    | 文本文件 | None  | 需要转换编码的单个文件 | `gbk2utf-8.py -f /Users/GcsSloop/Demo.txt`
`-d` | dir     | 文件夹   | None  | 需要转换编码的文件夹  | `gbk2utf-8.py -f /Users/GcsSloop/DemoDir`
`-b` | bak     | 布尔变量 | True  | 是否生成备份文件      | `gbk2utf-8.py -b False`
`-r` | restore | 布尔变量 | False | 是否恢复备份文件      | `gbk2utf-8.py -r True`
`-c` | clear   | 布尔变量 | False | 是否删除备份文件      | `gbk2utf-8.py -c True`


## 配置环境

想要使用该脚本必须保证python环境中一景存在以下几个模块

模块名称 | 摘要     | 导入方式
--------|---------|----------------------
chardet | 编码识别 | pip install chardet
click   | 参数解析 | pip install click

## 使用示例

该示例中分别执行了，转换单个文件，从备份文件恢复，清空备份文件，转换当前目录所有文件编码。

![](http://ww1.sinaimg.cn/large/005Xtdi2jw1f51om9rti9j30rs0gzgpn.jpg)

## 辅助优化

[在任意位置执行该脚本文件](https://github.com/GcsSloop/MacDeveloper/blob/master/Skill/RunPython.md)

## License
```
Copyright (c) 2016 GcsSloop

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
