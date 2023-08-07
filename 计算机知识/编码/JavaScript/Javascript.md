## 闭包

>闭包 = 函数 + 函数能够访问的自由变量

举个例子：

```js
var a = 1;

function foo() {
    console.log(a);
}

foo();
```

```js
var data = [];

for (var i = 0; i < 3; i++) {
  data[i] = function () {
    console.log(i);
  };
}

data[0]();
data[1]();
data[2]();
```

答案是都是 3
