# Mac环境变量设置

## 环境变量的位置

位置              | 级别      | 读写权限 | 摘要
------------------|-----------|----------|----
/etc/paths        | 1(系统级) | root     | 文件，每一行代表一个环境变量，不建议修改
/etc/paths.d/xxx  | 2(系统级) | root     | 文件夹， 可以在里面建任意不带后缀名的文件， 在文件中写入环境变量， 系统级环境变量建议放在该文件夹中
~/.bash_profile   | 3(用户级) | 用户     | 文件，`~` 代表当前用户目录，该文件可能不存在，不存在创建一个即可

**说明:**
> 
* 1.级别数字代表读取顺序，**数值越的优先读取**。环境变量文件读取顺序: `paths -> paths.d -> .bash_profile `
* 2.级别数字代表执行顺序，**数值高的优先执行**。若条命令在 用户级 和 系统级 里面均有，优先执行用户级命令。

## 设置环境变量

**对于系统级环境变量设置需要root用户权限，具体可以参见这篇文章 [获取Root权限](https://github.com/GcsSloop/MacDeveloper/blob/master/Skill/Root.md)**

### /etc/paths

paths 文件每一行代表一个环境变量，如下:

> PS:不建议修改该文件

```
/usr/local/bin
/usr/bin
/bin
/usr/sbin
/sbin
```

### paths.d

paths.d 是一个文件夹, 你可进入到其中创建任意名称的文件，然后将环境变量写入在其中。

**当前 PATH 如下:**

![](http://ww2.sinaimg.cn/large/005Xtdi2gw1f4jngyjyosj30fu0a60tq.jpg)

**进入到 paths.d 目录并创建 hello 文件:**

>
* 文件名可以任意取，尽量取有意义的名称，如配置 Python 环境就起名叫做 python 即可，没有后缀名
* 创建文件需要root权限，可以看到，没有root权限会报错
* 最后一条命令是进入编辑，这里使用的是 nano 界面相对比较友好(`^` 代表 control ) ，如果你对 vim 熟悉，用 vim 也可以

![](http://ww3.sinaimg.cn/large/005Xtdi2gw1f4jnnf0xb9j30fu0a6js5.jpg)

在里面输入路径，完成后按 control + x 退出，如果提示你保存，输入 y 回车即可保存。

![](http://ww1.sinaimg.cn/large/005Xtdi2gw1f4jnvcrhjvj30fu0a63zb.jpg)

完成之后新建一个终端页面，查看 PATH 发现已经配置成功了，多出来了 '/Users/GcsSloop' 这个环境变量:

![](http://ww1.sinaimg.cn/large/005Xtdi2gw1f4jny5mdhfj30fu0a6gmo.jpg)

