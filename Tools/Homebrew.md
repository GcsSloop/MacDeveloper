# Homebrew

Homebrew 是一款开源的软件包管理工具，可以方便的安装、升级、备份、管理你的电脑软件，实在是软件管理好帮手。

Homebrew 直接翻译是 **家酿，自制** 的意思，一般指酿造 红酒 白酒 等， 家酿的酒， 各家的口味都会不相同， 软件也是一样，每个人都有自己风格的配置， 自然也是各不相同的， homebrew 只提供酿造(安装) 的方法， 大家可以组合出各种各样风格的软件集， 这样一想的话， 名字还是挺贴切的。

顺便穿插一件趣事，在2015年的时候，Homebrew作者Max Howell应聘Google职位时，因为没有在白板上写出反转二叉树而被拒，在Twitter吐槽: 

>
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so f*** off.
（Google：我们90%的工程师都在用你的软件（Homebrew），但是你不会在白板上翻转二叉树所以滚出去）

这件事情在网上引发了关于招聘程序员面试时白板编程意义的讨论，想必很多程序员还有印象吧。

## Homebrew 与 Homebrew Cask

说到 Homebrew 就不得不提到 Homebrew Cask， 看两者名字就知道它们必然是有关联的， 两者都是软件包管理程序， 不同的是 Homebrew Cask 多了一个 Cask(木桶), 也就是说 Homebrew Cask 管理的是已经包装好的酒， 而 Homebrew 管理的是原液，没有包装过的，如下:

工具          | 摘要
--------------|----------------------
HomeBrew      | 会下载源码解压自动编译，并包含相关的依赖库，配置好环境变量，常用于安装配置开发环境，如 python、 ffmpeg 等
HomeBrew Cask | 下载已经编译好的应用包，然后解压并放置到统一到文件夹中，省去自己 下载 解压 安装 的麻烦，如 chrome、 github-desktop 等

>
#### 两者大致可以用是否带图形化界面来区分，但也不绝对。

## 优势

* 安装升级方便
* 自动配置环境
* 卸载比较干净

## 如何安装

### 1.安装HomeBrew

打开终端，输入:

``` shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

安装 HomeBrew 可能需要 Xcode，不过不需要担心，如果没有的话，它会提示你进行安装。

另外它支持的版本是 10.5 以上， 更多请参考 [**HomeBrew官网**](http://brew.sh/index_zh-cn.html)

### 2.安装HomeBrew Cask

如果你已经安装好了HomeBrew，打开终端，输入：

```
brew tap phinze/homebrew-cask
brew install brew-cask
```

就这样就安装完成啦。

## 如何使用

homebrew 与 homebrew cask 命令有很多类似之处，通常的格式如下：

```
brew <命令> <参数>
brew cask <命令> <参数>
```

**PS: 其中某些命令是没有参数的。详情见下面常用命令。**

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
******************** | **************************************************** 
brew home            | 打开homebrew官网
brew list            | 列出所有已经安装的内容
brew list --versions | 列出所有已经安装的内容，包括版本号
brew update          | 更新homebrew自身
brew outdated        | 检查是否有软件包需要更新
brew cleanup         | 清除旧版本缓存

### 2.HomeBrewCask

homebrewcask的命令与homebrew基本是一样的,以github官方客户端(github-desktop)为例:

命令                                | 摘要
------------------------------------|--------------------------------
brew cask search git*               | 搜索名称包含git的软件(*表示通配)，在结果里面有github-desktop
brew cask install github-desktop    | 安装github-desktop
brew cask uninstall github-desktop  | 卸载github-desktop
brew cask info github-desktop       | 显示github-desktop相关信息
*********************************** | **************************************************** 
brew cask home                      | 打开homebrew cask官网
brew cask list                      | 列出所有已经安装的软件
brew cask list --versions           | 列出所有已经安装的软件，包括版本号
brew cask update                    | 更新homebrew cask自身
brew cask outdated                  | 检查是否有软件包需要更新
brew cask cleanup                   | 清除旧版本缓存

>
**homebrew cask并没有提供更新软件的方法，更新软件只需要重新install一次就行了。**

