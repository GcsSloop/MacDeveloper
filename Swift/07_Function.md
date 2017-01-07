## 函数

- 函数定义的格式

```swift
func 函数名(形参列表) -> 返回值类型 {
  // 函数体
}
```

```swift
func sum(num1: Int, num2: Int) -> Int {
    return num1 + num2
}
```

- 没有返回值函数

```swift
func 函数名(形参列表) -> Void {
  // 函数体
}

func 函数名(形参列表) -> () {
  // 函数体
}

func 函数名(形参列表) {
  // 函数体
}
```

- 没有形参的函数小括号也不能省略

```swift
func 函数名() -> Int {
  // 函数体
}
```

- 返回元组类型

```swift
func getPoiny() -> (Int, Int) {
  return (10, 10)
}
```

```swift
 func find(id: Int) -> (name: String, age: Int){
    return ("Jack", 20)
}

var people = find(id: 2)

print("name=\(people.name), age=\(people.age)")
```

- 外部参数名可以在调用的时候提醒参数类型

```swift
func (外部参数名 形式参数名: 形式参数类型) -> 返回值类型 {
  // 函数体
}
```

```swift
func find( NO id: Int) -> (name: String, age: Int){
    return ("Jack", 20)
}

// 注意这里和上一个例子的不同之处
var people = find(NO: 2)

print("name=\(people.name), age=\(people.age)")
```

- 默认参数值

  可以在定义函数的时候给参数一个默认值 

```swift
func add(name: String, age: Int = 20) {
    print("添加：name = \(name), age=\(age)")
}

add(name: "Jack")
```

- 给参数一个下划线，可以在调用时不声明参数名

```swift
func add(_ name: String, age: Int = 20) {
    print("添加：name = \(name), age=\(age)")
}

add("Jack")
```

- 常量参数

  默认情况下，参数是一个常量(let)，不能修改。 

```swift
 func append(source: String, suffix: String) -> String {
    var source = source
    source += suffix
    return source
}

var str = append(source: "Hello ", suffix: "Swift")

print(str)
```

