## Python脚本: env: python\r: No such file or directory

在 Window 系统下写好的 Python 脚本放到 Linux 或者 OS X 系统下可能会出现如下问题。

### 错误原因

换行符问题 Windows 系统的换行符是 `\r\n` 而 Linux 与 OS X 则是 `\n` 所以执行第一行 `#!/usr/bin/env python`  读取到换行部分就会出错。

### 解决方法

#### vim

执行命令:
```
:set fileformat=unix 
:set fileformat=dos
```

#### SublimeText

选择菜单:
```
View > Line Endings > Unix
```
