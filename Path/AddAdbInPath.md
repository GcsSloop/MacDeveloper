# 添加 adb 到环境变量

## 1.找到 SDK 到本地路径

**然后找到 SDK 中 platform-tools 这一文件夹并记下路径。**
我的路径如下：
```
/Users/GcsSloop/Library/Android/sdk/platform-tools
```

## 2.找到配置文件

> 新建终端的文件夹路径默认在用户目录下，不需要切换到其它路径

在终端中依次输入以下两条命令:

```
  // 确保用户目录下存在 .bash_profile 这个文件
  touch .bash_profile
  // 打开这个文件
  open -e .bash_profile

```

## 3.添加路径

打开了 .bash_profile 文件后如果其中有内容在在后面追加以下内容：

```
  // 格式为 冒号(英文) 路径
  :/Users/GcsSloop/Library/Android/sdk/platform-tools
```

如果是一个空白文档，则输入以下内容:
```
  // 分割符是冒号(英文)
  export PATH=${PATH}:/Users/GcsSloop/Library/Android/sdk/platform-tools
```

保存并关掉文件。

## 4.使文件立即生效

在终端中输入以下命令，以便让更改的内容立即生效:
```
  source .bash_profile
```

## 5.确认结果

在终端中输入 `adb` 这个命令，如果出来的是一大堆内容，而不是 `command not found` 就说明环境变量配置成功了。




