## 输入输出参数

- 输入输出参数，顾名思义，能输入一个值进来，也能输出一个值到外部。
- swift 可以利用输入输出参数在函数内部修改外部变量的值。
- 有点类似于于OC的指针

### 1 定义方式

使用 inout 来定义。

```swift
func change( num: inout Int){
    num = 20
}

var a = 10
change(num: &a)
print(a)
```

```swift
func swap(num1: inout Int, num2: inout Int) {
    let temp = num1
    num1 = num2
    num2 = temp
}

// 不使用第三方变量 - 加减
func swap2(num1: inout Int, num2: inout Int) {
    num1 += num2
    num2 = num1 - num2
    num1 = num1 - num2
}

// 不使用第三方变量 - 异或
func swap3(num1: inout Int, num2: inout Int) {
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
}

var n1 = 10, n2 = 20

swap(num1: &n1, num2: &n2)

print(n1)
print(n2)
```

- 输入输出参数，不能将常量或者数值直接作为参数输入
- 输入输出参数，不能设置默认参数

### 2 输入输出参数的价值

- 实现多返回值(使用元组也可以)