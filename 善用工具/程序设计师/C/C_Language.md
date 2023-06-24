---
title: C_Language
permalink: clanguage.html
theme: jekyll-theme-cayman
---


# struct 结构体
在C语言中，可以使用结构体来定义和创建结构。结构体是一种用户自定义的数据类型，它可以包含多个不同类型的数据成员，这些数据成员可以是基本类型、数组、指针等。

下面是一个简单的例子，演示如何定义和创建一个结构体：

```c
#include <stdio.h>

// 定义结构体
struct Person {
    char name[20];
    int age;
    float height;
};

int main() {
    // 创建结构体变量
    struct Person person1 = {"John", 25, 1.75};
    
    // 访问结构体成员
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Height: %.2f\n", person1.height);
    
    return 0;
}
```

在上面的例子中，我们定义了一个名为`Person`的结构体，它包含三个数据成员：`name`、`age`和`height`。然后，我们在`main`函数中创建了一个名为`person1`的结构体变量，并初始化了它的数据成员。最后，我们访问了`person1`的数据成员，并在控制台上输出了它们的值。

注意，结构体变量的创建必须在函数内部或全局作用域内进行。在函数内部创建的结构体变量只能在该函数内部使用，而在全局作用域内创建的结构体变量可以在整个程序中使用。