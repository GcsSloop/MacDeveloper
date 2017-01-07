## 元组类型

### 1 元组定义

元组类型由N个人一类型的数据组成(N >= 0)

组成元组类型的数据可以称为元素。

```swift
let position = (x:105, y:20)

let pos = (name : "Jack")
```

### 2 元素访问

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

