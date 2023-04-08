## Python正则表达式操作指南

> 使用 re 模块

  ### 字符匹配


- \d  匹配任何十进制数；它相当于类 [0-9]。
- \D  匹配任何非数字字符；它相当于类 [^0-9]。
- \s  匹配任何空白字符；它相当于类  [ \t\n\r\f\v]。
- \S  匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
- \w  匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
- \W  匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。

### 重复

- \* 重复匹配之前的字母

- a/{1,3}b 将匹配 "a/b"，"a//b" 和 "a///b"。

### 使用正则表达式

- 编译正则表达式
正则表达式被编译成 `RegexObject` 实例，可以为不同的操作提供方法，如模式匹配搜索或字符串替换。

```
#python
>>> import re
>>> p = re.compile('ab*')
>>> print p
<_sre.SRE_Pattern object at 0xb76e1a70>
```

re.compile() 也接受可选的标志参数，常用来实现不同的特殊功能和语法变更。我们稍后将查看所有可用的设置，但现在只举一个例子：
```
#!python
>>> p = re.compile('ab*', re.IGNORECASE)
```

> 使用 raw 可以用来处理 `\` 的问题
如:  r"ab*" ,r"\\ab*"

### 执行匹配
一旦你有了已经编译了的正则表达式的对象，你要用它做什么呢？`RegexObject` 实例有一些方法和属性。这里只显示了最重要的几个，如果要看完整的列表请查阅 Python Library Reference

方法/属性	作用
- match()	决定 RE 是否在字符串刚开始的位置匹配
- search()	扫描字符串，找到这个 RE 匹配的位置
- findall()	找到 RE 匹配的所有子串，并把它们作为一个列表返回
- finditer()	找到 RE 匹配的所有子串，并把它们作为一个迭代器返回

如果没有匹配到的话，match() 和 search() 将返回 None。如果成功的话，就会返回一个 `MatchObject` 实例，其中有这次匹配的信息：它是从哪里开始和结束，它所匹配的子串等等。

MatchObject 实例也有几个方法和属性；最重要的那些如下所示：

方法/属性	作用
- group()	返回被 RE 匹配的字符串
- start()	返回匹配开始的位置
- end()	返回匹配结束的位置
- span()	返回一个元组包含匹配 (开始,结束) 的位置


在实际程序中，最常见的作法是将 `MatchObject` 保存在一个变量里，然後检查它是否为 None，通常如下所示：
``` python
#!python
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
print 'Match found: ', m.group()
else:
print 'No match'
```

### 模块级函数
你不一定要产生一个 `RegexObject` 对象然后再调用它的方法；re 模块也提供了顶级函数调用如 match()、search()、sub() 等等。这些函数使用 RE 字符串作为第一个参数，而后面的参数则与相应 `RegexObject` 的方法参数相同，返回则要么是 None 要么就是一个 `MatchObject` 的实例。
```
#!python
>>> print re.match(r'From\s+', 'Fromage amk')
None
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
<re.MatchObject instance at 80c5978>
```