## go

![](images/2022-11-16-18-38-57.png)

### 入门

![](images/2022-11-16-18-53-26.png)

#### hello,world

![](images/2022-11-16-18-54-15.png)

#### 命令行 参数
![](images/2022-11-16-18-55-35.png)


### 结构
![](images/2022-11-16-19-32-41.png)

#### 变量
![](images/2022-11-17-07-47-14.png)

人也是变量
![](images/2022-11-17-07-47-46.png)

> 短变量声明
![](images/2022-11-17-07-48-38.png)


#### 常量

![](images/2022-11-17-16-06-14.png)

```go
package main

import "fmt"

func main() {
   const LENGTH int = 10
   const WIDTH int = 5  
   var area int
   const a, b, c = 1, false, "str" //多重赋值

   area = LENGTH * WIDTH
   fmt.Printf("面积为 : %d", area)
   println()
   println(a, b, c)  
}
```

#### 运算符
![](images/2022-11-17-16-09-24.png)

```
+	 -	 *	 /	 %
```


#### 条件

![](images/2022-11-17-16-09-49.png)


#### 循环

![](images/2022-11-17-16-10-43.png)

#### 函数
![](images/2022-11-17-16-24-15.png)

```go
func function_name( [parameter list] ) [return_types] {
   函数体
}
```

#### 数组
![](images/2022-11-17-16-26-36.png)
```go
var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
```

#### 指针
![](images/2022-11-17-16-27-45.png)

#### Map(集合)
![](images/2022-11-17-16-30-23.png)

```go
package main

import "fmt"

func main() {
    var countryCapitalMap map[string]string /*创建集合 */
    countryCapitalMap = make(map[string]string)

    /* map插入key - value对,各个国家对应的首都 */
    countryCapitalMap [ "France" ] = "巴黎"
    countryCapitalMap [ "Italy" ] = "罗马"
    countryCapitalMap [ "Japan" ] = "东京"
    countryCapitalMap [ "India" ] = "新德里"

    /*使用键输出地图值 */
    for country := range countryCapitalMap {
        fmt.Println(country, "首都是", countryCapitalMap [country])
    }

    /*查看元素在集合中是否存在 */
    capital, ok := countryCapitalMap [ "American" ] /*如果确定是真实的,则存在,否则不存在 */
    /*fmt.Println(capital) */
    /*fmt.Println(ok) */
    if (ok) {
        fmt.Println("American 的首都是", capital)
    } else {
        fmt.Println("American 的首都不存在")
    }
}
```