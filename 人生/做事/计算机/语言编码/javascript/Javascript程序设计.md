---
title: javascript程序设计
permalink: javascript.html
theme: jekyll-theme-cayman
---

### 数据转换

| 方法         | 描述                                               |
|--------------+----------------------------------------------------|
| toString()   | 把对象的值转化为字符串                             |
| toFixed()    | 把数字转换为字符串，结果的小数点后有指定位数的数字 |
| parseFloat() | 解析一个字符串，并返回一个浮点数                   |
| parseInt()   | 解析一个字符串，并返回一个整数                     |
	
### 时间处理 Date 对象
> 自定义日期 Date("2021-03-04 22:23:00");

| 方法              | 描述                                      |
|-------------------+-------------------------------------------|
| getDate()         | 从 Date 对象返回一个月中的某一天 (1 ~ 31) |
| getDay()          | 从 Date 对象返回一周中的某一天 (0 ~ 6)    |
| getFullYear()     | 从 Date 对象以四位数字返回年份            |
| getHours()        | 返回 Date 对象的小时 (0 ~ 23)             |
| getMilliseconds() | 返回 Date 对象的毫秒 (0 ~ 999)            |
| getMinutes()      | 返回 Date 对象的分钟 (0 ~ 59)             |
| getMonth()        | 从 Date 对象返回月份 (0 ~ 11)             |
| getSeconds()      | 返回 Date 对象的秒数 (0 ~ 59)             |
| getTime()         | 返回1970年1月1日至今的毫秒数              |

### 查找
#### 匹配查找
```js
"youare pttpme".indexOf("http")
```
#### 正则查找
/正则表达式主体/修饰符(可选)


| 修饰符 | 描述                                                 |
|--------+------------------------------------------------------|
| i      | 执行对大小写不敏感的匹配                             |
| g      | 用于替换中，全部替换 |
| m      | 执行全局匹配多行匹配 |

``` js
//返回查找到的地方，没有则-1
var str = "Visit Runoob!"; 
var n = str.search(/Runoob/i);
//相同效果
var pattern1=/http/;
var pattern2=new RegExp("http");
pattern1.test("http://www.google.com")
```

####  验证与替换
``` 
//邮箱
var isemail=(/^/w+((-/w+)|(/./w+))*/@[A-Za-z0-9]+((/.|-)[A-Za-z0-9]+)*/.[A-Za-z0-9]+$/)

//手机号
1. <input onkeydown="this.value=this.value.replace('/\D/g','');" maxlength="11"/>

2. function inputmobile(obj) {
    obj.value = obj.value.replace(/\D+/g,'');
    if (obj.value.length >=11) { 
        obj.value = obj.value.substr(0,11);
        var myreg = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/g; 
        if(!myreg.test(obj.value)) {
            obj.value = '请输入正确的手机号';
        }  
    }
}
```

## 获取文件名
``` js
var url = window.location.pathname;
var filename = url.substring(url.lastIndexOf('/')+1);
```
## 正反斜杠转换
``` js
replace(/\\/g,'/');//替换"\"为"/"
```
# 提高性能
## 合并脚本
## 压缩
## 利用CDN加速

``` html
<script>window.jQuery || document.write('<script src="js/vendor/jquery-1.10.2.min.js"></script>')</script>
```
## blob 转 file

```js
const files = new window.File(
    [blob],
    this.files[0].name,
    { type: this.files[0].type }
);
```


## 时间不足10位补0方案
``` js
  //创建补0函数
     function  bu0(s) {
         return  s < 10 ?  '0'  + s: s;
```

