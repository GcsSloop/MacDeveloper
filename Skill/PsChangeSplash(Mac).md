# 更改PS启动界面

作为一个应用的启动页，虽然并没有什么用处，但换一个好看一点的界面会让人的心情更加舒畅，更有工作学习的动力。

先上效果图:

![](http://ww1.sinaimg.cn/large/005Xtdi2jw1f5qdmfgj1rj31400p07f2.jpg)

## 所需工具

由于PS(MAC版)的所有资源被封装成了一个后缀名为 .rsrc 的单个文件，但是这个文件的解析工具太难找了，找了半天才找到这样一个工具

### 开源项目地址: [ResKnife](https://github.com/slobo/ResKnife)

### 直接下载地址: [原版]() | [个人修改版]()

> PS：由于原版图标实在是太丑了，本人就简单的替换了应用图标和资源文件图标，做了一个个人修改版。

## 替换方法

替换方法非常简单，大致如下：

### 1.找到资源文件

资源文件位置在 `/Applications/Adobe Photoshop CS6/Adobe Photoshop CS6.app/Contents/Resources`

在Finder的应用程序目录下找到Adobe Photoshop CS6.app, 右键 -> 显示包内容 即可看到里面的内容，在`/Contents/Resources`目录能找到一个名为 `Adobe Photoshop CS6.rsrc` 的资源文件。


