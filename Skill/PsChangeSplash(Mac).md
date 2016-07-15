# Mac更改Photoshop(PS)启动界面

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

作为一个应用的启动页，虽然并没有什么用处，但换一个好看一点的界面会让人的心情更加舒畅，更有工作学习的动力，之前的Windows上面替换比较容易，可惜换了Mac之后就找不到替换的方法了，基本找不到教程，不仅如此，甚至连相关的工具都鲜有人知，我也是扒了好几天论坛才找到的解决方案，为了方便其他有类似需求的小伙伴，特此做一个简单的替换教程。

先上效果图(图是我自己做的):

![](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/01.png)

## 注意事项

**请不要手动为你的 rsrc 文件替换图标(即不要使用官方推荐的替换图标方式)，否则原先可直接编辑的内容会整个变成 Data Fork 一个文件，请谨记。若想自定义，请先制作icns格式的图标，使用该图标替换掉 ResKnife 中的资源图标，之后重启 ResKnife 和 Finder 即可。**


## 所需工具

由于PS(MAC版)的所有资源被封装成了一个后缀名为 .rsrc 的单个文件，但是这个文件的解析工具太难找了，很多都不能用，找了好久才找到这样一个历史悠久但不太著名的工具:

### 开源项目地址: [ResKnife](https://github.com/slobo/ResKnife)

### 直接下载地址: [原版](https://github.com/downloads/slobo/ResKnife/ResKnife%20Cocoa.zip) | [个人修改版](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/ResKnife%20Cocoa.app.zip)

> PS：由于原版图标实在是太丑了，本人就简单的替换了应用图标和资源文件图标，做了一个个人修改版。

## 替换方法

替换方法非常简单，大致如下：

### 1.找到资源文件

资源文件路径(具体应该取决与你的安装位置)： `/Applications/Adobe Photoshop CS6/Adobe Photoshop CS6.app/Contents/Resources`

在Finder的 `应用程序` 目录下找到 `Adobe Photoshop CS6.app`, **右键 -> 显示包内容** 即可看到里面的内容，在 `/Contents/Resources` 目录下一个名为 `Adobe Photoshop CS6.rsrc` 的资源文件就是我们需要的文件，这个图标是我替换的(**请不要自己随意替换，回去看前面的注意事项**)，在其他电脑上显示可能不同，认准名称即可。

![](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/02.png)

**PS: 建议先备份一下资源文件，再进行修改，以便出错时可以替换回原文件。**

### 2.打开文件找到需要替换的目标

使用 ResKnife 打开 Adobe Photoshop CS6.rsrc 后可能会弹出多个窗口，从里面资源文件显示比较多的窗口找到一个名为 SplashExtendedBackground.png 的文件，这个就是我们需要的文件。

![](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/03.png)

### 3.导出内容(可选)

使用上图中的导出按钮可以导出启动界面的图片，格式为png，然后对这个图片进行编辑，如果你已经有了完成好的启动界面图片，可以跳过该步骤。

**PS: 如果导出按钮找不到，可以从菜单栏 Windows -> Customize Toolbar 来给菜单栏添加这个选项。**

### 4.编辑

从该软件的菜单栏上可以看到两个编辑按钮，我们此处使用上图中标注的 Edit Hex 即可，由于该选项编辑的是十六进制内容，所以打开后是这样的:

![](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/04.png)

**我们先将其中的内容全部删除，但不要关闭这个窗口。**

## 5.替换

找到编辑完成的 .png 文件，并将后缀名改为 .rsrc ，同样使用 ResKnife打开，双击 Data Fork 这一项目，同样弹出一个十六进制窗口，将里面的东西全部复制粘贴到上一步删除了内容的窗口中，之后保存退出即可。


## 修改好的资源文件

### 我使用的原图：

![](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/SplashExtendedBackground.png)

### [替换完成的资源文件(适用于Photoshop CS6)](https://raw.githubusercontent.com/GcsSloop/MacDeveloper/res/Skill/res/PsChangeSplash(Mac)/Adobe%20Photoshop%20CS6.rsrc)

## About Me

一名生活在 2.5 次元的 Android 开发者。

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

<a href="https://github.com/GcsSloop/README/blob/master/README.md" target="_blank"> <img src="http://ww4.sinaimg.cn/large/005Xtdi2gw1f1qn89ihu3j315o0dwwjc.jpg" width=300 height=100 /> </a>
