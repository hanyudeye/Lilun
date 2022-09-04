---
title: Learn Python
permalink: learn-python.html
theme: jekyll-theme-cayman
---

## vscode 执行 python 中文乱码

1. 设置环境变量  PYTHONIOENCODING=utf-8

## 正则表达式
> 操作文本或数据是一件大事

 re  模块

- 匹配开头 match()
- 匹配整个字符串search()
-  compile()


## 对象类型

| 对象类型         | 例子                                  |
| ---------------- | ------------------------------------- |
| 数字             | 123, 2.123,3+4j,complex(12,3),Decimal |
| 字符串           | 'span' , "gui's" ,                    |
| 列表             | [1,[2,'three'],4]                     |
| 字典             | {'food':'鸡腿','taste':'very good'}   |
| 元组             | (1,'fuck',3)                          |
| 文件             | myfile=open('txt','r')                |
| 集合             | set('abc),{'1','bb','c'}              |
| 其它类型         | None, 布尔型                          |
| 编程单元类型     | 函数、模块、类                        |
| 与实现相关的类型 | 编译的代码堆栈跟踪                    |

列表可以使用生成器生成:
```python
nums=[1,2,4,9]
列表=[ n+1 for n in nums]
```

### 自定义类

```python
class 类名:
    ...
```
### 继承类
```python
class 派生类名(基类名)
class SubClassName (ParentClass1[, ParentClass2, ...]):
```
## 对象行为
### 字符串
- len()
- s[:-1]
- s[0:3]
- s.find(x)
- s.replace(x,y)
- s.split(',')
- s.upper()
- s.isalpha()
- s.rstrip()

### 列表
- L.append(x)
- L.pop(x) 移除某一项
- L.sort()
- L.reverse() 倒序

### 元组(tuple)
- T.index(x) 查找 x 出现在元组的哪个位置
- T.count(x) 统计

### 字典
- D.keys()
- sorted(D) 返回排好序的键组

### 类型转换

- int(x [,base])
- long(x [,base])
- float(x)
- str(x)
- tuple(s)
- list(s)
- set(s)
- dict(d) d 必须是一个序列 (key,value)元组。
- frozenset(s)  转换为不可变集合
- chr(x) 将一个整数转换为一个字符
- unichr(x) 将一个整数转换为 Unicode 字符
- ord(x) 将一个字符转换为它的整数值
- hex(x) 将一个整数转换为一个十六进制字符串
- oct(x) 将一个整数转换为一个八进制字符串
### 运算符
#### 成员运算符 
 - in
 - not in
#### 身份运算符
 引用同一对象
 - is  x is y ,类似 id(x) == id(y)
 - is not  类似 id(x) != id(y)

### 自定义行为(函数)
``` python
def <name>(arg1,arg2,... argN):
    <statements>
```
## 控制流程

### 条件语句
``` python

if x < y:
    x=1
```
注意：省略了括号


### 循环 
```python
while True:
    x=1
```
## 重用代码 (模块，包)

### 模块的搜索路径 (顺序为)

- 1. 程序的主目录
- 2. PYTHONPATH目录
- 3. 标准链接库目录

## 异常处理

try/except 捕捉由python或你引起的异常并恢复

try/finally 无论异常是否发生，执行清理行为

raise 手动在代码中触发异常

assert 有条件在程序代码中触发异常

