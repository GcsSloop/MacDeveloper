# Swift 简介

Swift 是苹果公司设计的一个开源的开发语言。

## 1. 语法须知

### 1.1 基本常识

- 扩展名为 .swift
- 没有 main 函数，从上至下依次执行
- 不用在每一条语句后面加分号

### 1.2注释

```swift
// 单行注释

/*
 多行注释
 */
 
/*
 多行注释允许嵌套
 /*
  嵌套的多行注释
  */
 */
```

### 1.3变量和常量

- let 声明常量

  ```swift
  let PI = 3.14
  ```

- var 声明变量

  ```swift
  var age = 20, heigit = 175
  ```

### 1.4 Playground 的使用

可以即时的查看代码运行效果。

### 1.5 字符串操作

```swift
// 字符串拼接
var str = "123"
var str2 = "456"
vat dst = str + str2

// 插入变量
var age = 20
let str = "I am \(age) years old."
```

### 1.6 打印输出

```swift
print("")
println("")
```

### 1.7 常量和变量命名

#### 允许使用的内容

- 字母、数字
- 中文
- 特殊字符(𝜋)
- emoji表情(😂)

#### 不允许使用的内容

- 不能使用数学符号(+ - * /)
- 不能使用箭头(→)
- 不能使用特殊的无效字符
- 不能使用关键字
- 不能以数字开头
- 不能单独一个下划线 `_` 
- ...



## 2. 数据类型

### 2.1 Swift 常见数据类型

```swift
 Int Float Double Bool Character String
 Array Dictionary 元组类型(Tuple) 可选类型(Optional)
```

### 2.2 如何指定数据类型

变量名 : 数据类型

```swift
var age : Int = 10
```

- Swift 严格要求使用前必须初始化。
- 一般来说没有必要声明 变量、常量 的类型。
- Swift 会根据初始化内容自动判断数据类型。

### 2.3 整数

- 整数类型分两种

  - 有符号 (signed)：正、负、零
  - 无符号(unsigned)：正、零

- Swift 提供 8位、16位、32位、64位 有符号 和 无符号整数(相当于有8种整数类型)

  - UInt8：8位无符号整型
  - Int32：32位有符号整型

- 最值(使用 min 和 max 来获取某个类型最大值和最小值)

  ```swift
  let minValue = UInt8.min
  let maxValue = UInt8.max
  ```

- Int 和 UInt

  - Swift 提供了特殊的有符号整数类型(Int)和无符号整数类型(UInt)。
  - Int\UInt 长度于当前系统平台一致，在32位系统上占有32位，在64位系统上占用64位。

- 整数运算

  - 不同长度不允许相加。
  - 有符号和无符号不允许相加。
  - 在通常情况下建议使用默认变量类型(Int)。

- 存储范围

  - 每种数据类型都有自己的取值范围。
  - 如果赋值超过了范围会直接报错。

- 表示形式

  - 十  进制：没有前缀 (let a = 10)
  - 二  进制：0b作为前缀 (let b = 0b1010)
  - 八  进制：0o作为前缀 (let c = 0o12)
  - 十六进制：0x作为前缀 (let d = 0xA)

### 2.4 浮点数

- Swift提供了两种类型的浮点数
  - Float ：32位
  - Double：64位
- 精确程度
  - Float：至少6位小数
  - Double：至少15位小数
- 如果没有明确说明类型，浮点数默认类型是 Double
- 表示形式
  - 十进制(没有前缀)
    - 没有指数：let a = 12.5
    - 有指数： let b = 0.125e2
      - MeN = M * 10的N次方
  - 十六进制(0x前缀，一定要有指数)
    - let c = 0xC.8p0  // 0xC.8 * 2^0 = 12.5 * 1
      - 0xMpN = 0xM * 2的N次方

### 2.5 数字格式

**可以增加额外的0**

```swift
let money = 0001999
```

可以增加额外的下划线

```swift
let money = 100_0000
let momey2 = 1_000_000
```

### 2.6 类型转换

使用 数据类型(数据) 进行转化类型。

```swift
let a:Int8 = 12
let b:Int = 15
let c = Int(a) + b
```

### 2.7 类型别名

可以使用 `typealias` 关键字来定义类型别名。

```swift
typealias Age = Int
var xiaoming:Age = 8
```



## 3. 运算符

#### 3.1 Swift 支持的部分运算符

- 赋值运算符 = 
- 复合运算符 +=、 -=
- 算数运算符 +、-、*、／
- 求余运算符 %
- 自增、自减运算符 ++、 --
- 比较运算符 ==、!=、>、<、>=、<=
- 逻辑运算符 &&、||、 !
- 三目运算符 ? :
- 范围运算符 ..<、 ...
- 溢出运算符 &+、&-、&*、&／、&%

#### 3.2 赋值运算符

**1对1赋值**

```swift
var a = 5
```

**N对N赋值**

```swift
var (a,b) = (4,5)
```

**Swift 赋值没有返回值**

不允许连等，即这种写法是错误的 `var a = b = 2` 

#### 3.3 求余运算符

求余运算也叫取模运算。

- 9 % 4  // 1
- -9 % 4 // -1
- 9 % -4 // 1
- -9 % -4 // -1

符号正负取决于左侧。

**Swift 支持浮点数(小数)的取模**

- 8 % 2.5 // 0.5

#### 3.4 Bool(布尔类型)

- true 真
- false 假

swift 只有Bool类型才能判断真假，  
if语句的条件只能是Bool类型。

**比较运算符／逻辑运算符／三目运算符**

- 比较运算符／逻辑运算符 会返回 Bool 类型的值。
- 三目运算符的条件必须是Bool类型。

#### 3.5 范围运算符

范围运算符用来表示一个范围，有2种类型的范围运算符

- 闭合范围运算符：a...b ，表示 [a, b]，包含 a 和 b
- 半闭合范围运算符：a..<b， 表示[a, b)，包含a，不包含b

```swift
for i in 0..<5 {
    print(i)
}
```

#### 3.6 溢出运算符

每种数据类型都有自己的取值范围，在默认情况下，一旦赋值超出了取值范围，会产生编译或者运行时错误。

Swift 为整形计算提供了5个以&开头的一处运算符，能对超出取值范围的数值进行灵活处理。

**值的上溢出**

```swift
let x = UInt8.max
let y = x &+ 1
```

y 最终结果为 0。

**值的下溢出**

```swift
let x = UInt8.min
let y = x &- 1
```

y最终结果为 255。

除零溢出

```swift
let x = 10 &/ 0
let y = 10 &% 0
```

x 和 y 结果均为 0



## 4. 元组类型

### 4.1 元组定义

元组类型由N个人一类型的数据组成(N >= 0)

组成元组类型的数据可以称为元素。

```swift
let position = (x:105, y:20)

let pos = (name : "Jack")
```

### 4.2 元素访问

根据名称访问

```swift
var point = (x:10, y:20)
point.x
point.y
```

使用位置下标访问

```swift
var point = (x:10, y:20)
point.0
point.1
```

也可以直接更改

```swift
var point = (x:10, y:20)
point.x = 30
point.y
```

如果使用let定义表示所有元素都是常量，不可更改。

可以直接打印元组。

```swift
var point = (x:10, y:20)
print(point)
```

可以省略元素名称。

```swift
var point = (10, "jack")
point.0
point.1
```

可以明确指定元素类型

```swift
var person : (Int, String) = (20, "Jack")
```

指定元素类型的情况下不能添加元素名称。

可以使用多个变量接收元组数据。

```swift
var (x, y) = (10, 20)
var point = (x, y)
```

可以将元素分别赋值给多个变量。

```swift
var point = (10, 10)
var (x, y) = point
```

可以使用 下划线_ 忽略某个元素的值，取出其他元素。

```swift
var person = (10, "Jack")
var (_, name) = person
```



## 5. 流程结构

### 5.1 Swift 支持的流程结构

- 循环结构： for、 for-in、while、do-while 
- 选择结构：if、switch

这些语句后面一定要添加上 `{}` 

### 5.2 for-in

```swift
for i in 1...3 {
  // TODO
}
```

如果不需要范围中的数值，可以用 `下划线_` 忽略

```
for _ in 1...3 {
  // TODO
}
```

### 5.3 Switch 

**特性：**

- swicth 的变量不需要小括号
- case 支持字符串等内容
- case 结尾不需要 break
- case 后面必须有一个可执行语句 

```swift
switch value {
    case "A":
        print("A")
    case "B":
        print("B")
    default:
        break
}
```
