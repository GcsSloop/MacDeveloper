# 在任意位置运行Python脚本

**本方法适用于 OS X 和 Linux 系统!**

python 作为一门简单而有强大的语言，在生活学习中帮助我们处理一些重复枯燥的事情的确是一种不错的选择。

## 默认运行方式
一般来说我们运行python都需要像下面这样:

> 在python文件所在目录:
```
python hello.py
```

## 简化

> 我们可以简化一下，让其在python文件所在目录可以直接运行，如下:
```
hello.py
```

想要这样做，我们需要标示其是一个python程序，在hello.py的第一行添加如下内容:

```
#!/usr/bin/env python
```

添加完之后还需要添加可执行权限，使用 `chmod` 命令：

```
chmod +x hello.py
```


## 在任意位置执行

想要其在任意位置执行，只需要将python文件所在目录添加进系统环境变量即可

OS X 系统环境变量设置可以参见 **[Mac环境变量设置](https://github.com/GcsSloop/MacDeveloper/blob/master/Skill/Path.md)** 这篇文章。

