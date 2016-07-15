# Homebrew

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

之前有一名叫做[littleMark](https://github.com/madongqiang2201)的小伙伴在Issues中建议我添加一些东西，不过那段时间比较忙，一直没有时间来处理这件事情，现在特地来处理一下这件事情，如果有其他的小伙伴有什么好的意见或者建议，欢迎在Issues中告诉我。

## 简介

Homebrew 是一款开源的软件包管理工具，可以方便的安装、升级、备份、管理你的电脑软件，实在是软件管理好帮手。

Homebrew 直接翻译是 **家酿，自制** 的意思，一般指酿造 红酒 白酒 等， 家酿的酒， 各家的口味都会不相同， 软件也是一样，每个人都有自己风格的配置， 自然也是各不相同的， homebrew 只提供酿造(安装) 的方法， 大家可以组合出各种各样风格的软件集， 这样一想的话， 名字还是挺贴切的。


顺便穿插一件趣事，在2015年的时候，Homebrew作者Max Howell应聘Google职位时，因为没有在白板上写出翻转二叉树而被拒，在Twitter吐槽: 
>
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so f*** off.
（Google：我们90%的工程师都在用你的软件（Homebrew），但是你不会在白板上翻转二叉树所以滚出去）

这件事情在网上引发了关于招聘程序员面试时白板编程意义的讨论，想必很多程序员还有印象吧。

## Homebrew 与 Homebrew Cask

说到 Homebrew 就不得不提到 Homebrew Cask， 看两者名字就知道它们必然是有关联的， 两者都是软件包管理程序， 不同的是 Homebrew Cask 多了一个 Cask(木桶), 也就是说 Homebrew Cask 管理的是已经包装好的酒， 而 Homebrew 管理的是原液，没有包装过的，如下:

工具          | 摘要
--------------|----------------------
Homebrew      | 会下载源码解压自动编译，并包含相关的依赖库，配置好环境变量，常用于安装配置开发环境，如 python、 ffmpeg 等
Homebrew Cask | 下载已经编译好的应用包，然后解压并放置到统一到文件夹中，省去自己 下载 解压 安装 的麻烦，如 chrome、 github-desktop 等

>
**两者大致可以用是否带图形化界面来区分，但也不绝对。**

* [**Homebrew 官网**](http://brew.sh/index_zh-cn.html)
* [**Homebrew Cask官网**](https://caskroom.github.io/)

## 优势

* 安装升级方便
* 自动配置环境
* 卸载比较干净
* 可以一次安装或者卸载多个软件
* 方便，方便，还是方便

## 如何安装

### 1.安装Homebrew

#### 环境要求

* 1.配备 英特尔(Intel) CPU 的MAC电脑。
* 2.系统版本在 10.9 以上，10.5 ~ 10.8 的系统可以安装 [Tigerbrew](https://github.com/mistydemeo/tigerbrew)。
* 3.有Command Line Tools for Xcode，使用 `xcode-select --install` 命令来安装，其实安装Xcode也可以。

在具备了以上条件后，在终端内输入:

``` shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 2.安装Homebrew Cask

如果你已经安装好了Homebrew，打开终端，输入：

```
brew tap caskroom/cask
brew install brew-cask
```

就这样就安装完成啦。


## 常用命令

### 1.Homebrew

以下以wget(一个下载工具)作为示例演示:

命令                 | 摘要
---------------------|--------------------------------
brew search wget     | 搜索名称包含wget的库(软件)
brew install wget    | 安装wget
brew uninstall wget  | 卸载wget
brew info wget       | 显示wget相关信息
brew deps wget       | 显示wget这个工具所依赖的其他库
brew upgrade wget    | 更新wget(更新时旧版本的安装包依旧会保存在你的电脑上)
                     | 
brew home            | 打开homebrew官网
brew list            | 列出所有已经安装的内容
brew list --versions | 列出所有已经安装的内容，包括版本号
brew update          | 更新homebrew自身
brew outdated        | 检查是否有软件包需要更新
brew cleanup         | 清除旧版本缓存

### 2.Homebrew Cask

homebrewcask的命令与homebrew基本是一样的,以github官方客户端(github-desktop)为例:

命令                                | 摘要
------------------------------------|--------------------------------
brew cask search git*               | 搜索名称包含git的软件(*表示通配)，在结果里面有github-desktop
brew cask install github-desktop    | 安装github-desktop
brew cask uninstall github-desktop  | 卸载github-desktop
brew cask info github-desktop       | 显示github-desktop相关信息
                                    | 
brew cask home                      | 打开homebrew cask官网
brew cask list                      | 列出所有已经安装的软件
brew cask list --versions           | 列出所有已经安装的软件，包括版本号
brew cask update                    | 更新homebrew cask自身
brew cask outdated                  | 检查是否有软件包需要更新
brew cask cleanup                   | 清除旧版本缓存

>
**homebrew cask并没有提供更新软件的方法，更新软件只需要重新install一次就行了。**

**PS: Homebrew 与 Homebrew Cask都支持批量安装软件，方式如下:**

```
brew install <软件1> <软件2> <软件3>
brew cask install <软件1> <软件2> <软件3>
```

## 结语

**如果本文中有什么错误或者纰漏，欢迎指正。**

## About Me

一名生活在 2.5 次元的 Android 开发者。

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

<a href="https://github.com/GcsSloop/README/blob/master/README.md" target="_blank"> <img src="http://ww4.sinaimg.cn/large/005Xtdi2gw1f1qn89ihu3j315o0dwwjc.jpg" width=300 height=100 /> </a>
