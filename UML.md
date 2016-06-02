# Mac 中使用 StarUML

作为一个程序员，拥有一个得心应手的 UML 绘制工具能够帮助你事半功倍的完成任务，也可以避免日后面对陈年老代码时抓耳挠腮，不知道自己曾经到底写了什么。

**这里推荐的是 StarUML 界面干净整洁，使用起来也很方便，而且是跨平台的， Mac Windows Linux 均有。**

下面是我用 StarUML 绘制的一个活动图:

![](http://ww4.sinaimg.cn/large/005Xtdi2jw1f4g9pwjrrzj30rs0k20v1.jpg)

## [官网下载](http://staruml.io/)

StartUML 是一款收费软件，如果各位有钱的话，在官网买一个许可，就当是赞助一下作者。

实在是没钱，可以考虑破解一下，破解方法见下面；

### 1.找到许可文件

```
安装目录/Contents/www/license/node/LicenseManagerDomain.js
```
>
Mac 的可以在 Finder 中应用程序目录下找到 StartUml.app 右键-> 显示包内容即可看到内部文件。

### 2.添加许可

添加完成后，保存退出。

```
function validate(PK, name, product, licenseKey) {
    var pk, decrypted;

    // 添加的内容****************
    return {
        name: "GcsSloop",
        product: "StarUML",
        licenseType: "vip",
        quantity: "mergades.com",
        licenseKey: "mKey"
    };
    // **************************
    
    try {
        pk = new NodeRSA(PK);
        decrypted = pk.decrypt(licenseKey, 'utf8');
    } catch (err) {
        return false;
    }
    var terms = decrypted.trim().split("\n");
    if (terms[0] === name && terms[1] === product) {
        return { 
            name: name, 
            product: product, 
            licenseType: terms[2],
            quantity: terms[3],
            licenseKey: licenseKey
        };
    } else {
        return false;
    }
}
```

### 3.获取许可

打开 StartUML

Help -> Enter License

分别输入:

```
Name    : GcsSloop
License : mKey
```

点 OK 即可获取权限。


