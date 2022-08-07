## php 字符串中是否包含指定字符串的多种方法

编写程序的时候，经常要处理字符串，最基本就是字符串的查找，在php检测字符串中是否包含指定字符串可以使用正则，如果你对正则不了解，那么有几个函数可以为您提供方便。

#### strpos() 函数判断字符串中是否包含某字符串

**1\. strstr**

strstr() 函数搜索一个字符串在另一个字符串中的第一次出现。  
该函数返回字符串的其余部分（从匹配点）。如果未找到所搜索的字符串，则返回 false。

代码如下:
```php
<?php
 /*如手册上的举例*/
 $email = 'user@example.com';
 $domain = strstr($email, '@');
 echo $domain;
 // prints @example.com
?>
```
**2\. stristr**

stristr() 函数查找字符串在另一个字符串中第一次出现的位置。  
如果成功，则返回字符串的其余部分（从匹配点）。如果没有找到该字符串，则返回 false。

它和strstr的使用方法完全一样.唯一的区别是stristr不区分大小写.

**3\. strpos**

strpos函数返回boolean值.FALSE和TRUE不用多说.用 “===”进行判断.strpos在执行速度上都比以上两个函数快,另外strpos有一个参数指定判断的位置,但是默认为空.意思是判断整个字符串.缺点是对中文的支持不好.

实例1
```php
if(strpos('www.jb51.net','jb51') !== false){ 
 echo '包含jb51'; 
}else{
 echo '不包含jb51'; 
}
```
实例2
```php
$str= 'abc';
$needle= 'a';
$pos = strpos($str, $needle); // 返回第一次找到改字符串的位置，这里返回为1，若查不到则返回False
```


**4\. explode**

用explode进行判断PHP判断字符串的包含代码如下:
```php
function checkstr($str){
 $needle ='a';//判断是否包含a这个字符
 $tmparray = explode($needle,$str);
 if(count($tmparray)>1){
 return true;
 } else{
 return false;
 }
}
```
**5、substr例如我们需要判断最后一个字符是不是制定字符**

```php
<?php
/*
$str1="<p>这是个winrar专用的dll然后下哦啊不错的dll文件，QlogWin32.dll</p>";
if(substr($str1,-8)==".dll</p>"){
echo substr($str1,0,-4);
}
```
**6、substr\_count统计“子字符串”在“原始字符串中出现的次数”**

substr\_count()函数本是一个小字符串在一个大字符串中出现的次数：  
$number = substr\_count(big\_string, small\_string);  
正好今天需要一个查找字符串的函数，要实现判断字符串big\_string是否包含字符串small\_string，返回true或fasle；

查了半天手册没有找到现成的函数，于是想到可以用substr\_count函数来实现代码如下：

```php

function check_str($str, $substr)
{
 $nums=substr_count($str,$substr);
 if ($nums>=1)
 {
  return true;
 }
 else
 {
  return false;
 }
}
```
超级简单！

具体的大家可以查找一下相关函数，进行高级应用。