# Mac原生支持ntfs格式移动硬盘的读写

本方法适用于 OSX 10.5 之后的系统。

## 1、插上硬盘

## 2、获取硬盘名称

硬盘名称就是显示名称，有时硬盘已经被挂载但不显示可以在**终端**中查看。

在终端中输入以下命令会显示出所有硬盘列表:

```
diskutil list
```
显示结果大致如下:

> PS: 我的移动硬盘名字是“魔法森林”，可以在最下面看到格式是Windows_NTFS。
```
GMBA:~ GcsSloop$ diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *121.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:          Apple_CoreStorage Macintosh HD            120.5 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
/dev/disk1 (internal, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS Macintosh HD           +120.1 GB   disk1
                                 Logical Volume on disk0s2
                                 369C6216-4C2D-48BA-A71D-1DA0F9C74EB8
                                 Unencrypted
/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *1.0 TB     disk2
   1:               Windows_NTFS 魔法森林                1.0 TB     disk2s1
```

## 3、创建或更新/etc/fstab文件

对fstab文件修改需要root用户权限，获取方式请参考**[［Root］](https://github.com/GcsSloop/MacDeveloper/blob/master/Root.md)**这篇文章。

### 切换到root模式
在终端界面输入 su 命令，在输入密码后切换到root用户模式：
> 在root模式下前面显示到是 sh-3.2# 

```
GMBA:~ GcsSloop$ su
Password:
sh-3.2# 
```
## 进入编辑页面
> 以下使用的vim编辑器，使用其它编辑器也可，例如nano

输入 vim /etc/fstab 命令使用vim编辑器编辑fstab文件：

第一次打开时内容应该是空白，如下:
```
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
"/etc/fstab" 1L, 1C
```

点击键盘字母i进入输入状态:

```
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- INSERT -- 
```

在其中输入以下内容：

```
LABEL=魔法森林 none ntfs rw, auto, nobrowse
```
格式为: LABEL=移动影片名称 none ntfs rw, auto, nobrowse

>PS: 如果移动硬盘名字里面有空格键，就需要用\040的意思是代替空格键，如：Gcs/040Sloop。<br/>
ntfs rw表示把这个分区挂载为可读写的ntfs格式。<br/>
nobrowse代表了在finder里不显示这个分区，这个选项非常重要，如果不打开的话挂载是不会成功的。<br/>

输入完成后先按左上角的esc按键，之后输入 “:wq”(全英文，没有引号)，保存退出文件。

```
LABEL=魔法森林 none ntfs rw, auto, nobrowse
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
:wq
```

## 4、拔掉硬盘再次插上即可

插上硬盘之后并不会显示，不过你可以通过以下方式找到它：

在Finder中使用快捷键 Command＋Shift＋G 之后在其中输入 /Volumes 点击前往，如下：

![](http://ww4.sinaimg.cn/large/005Xtdi2jw1f43pu45rnjj30bx045aa7.jpg)

![](http://ww3.sinaimg.cn/large/005Xtdi2jw1f43put9fmoj30le0c4my6.jpg)

## 5、可以将移动硬盘拖动到侧边栏建立快捷方式

我的已经放到侧边栏了，在上面到图片中可以看到，只需要拖动图标到侧边栏就能自动建立快捷访问方式。






