## 数据类型

### 1 Swift 常见数据类型

```swift
 Int Float Double Bool Character String
 Array Dictionary 元组类型(Tuple) 可选类型(Optional)
```

### 2 如何指定数据类型

变量名 : 数据类型

```swift
var age : Int = 10
```

- Swift 严格要求使用前必须初始化。
- 一般来说没有必要声明 变量、常量 的类型。
- Swift 会根据初始化内容自动判断数据类型。

### 3 整数

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

### 4 浮点数

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

### 5 数字格式

**可以增加额外的0**

```swift
let money = 0001999
```

可以增加额外的下划线

```swift
let money = 100_0000
let momey2 = 1_000_000
```

### 6 类型转换

使用 数据类型(数据) 进行转化类型。

```swift
let a:Int8 = 12
let b:Int = 15
let c = Int(a) + b
```

### 7 类型别名

可以使用 `typealias` 关键字来定义类型别名。

```swift
typealias Age = Int
var xiaoming:Age = 8
```

