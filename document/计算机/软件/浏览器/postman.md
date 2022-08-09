## 什么是 postman

postman 是为了更好的发送 web 表单


## 发送 ajax 请求的方法?
实现ajax必须依赖浏览器提供的XMLHttpRequest对象

在postman的header中指定X-Requested-With的值为XMLHttpRequest

> X-Requested-With:XMLHttpRequest
> 大小写不重要

另外，ajax请求需要指定Content-Type请求内容的类型格式,常用的格式指定为json

Content-Type:application/json

在Postman的header中完善上面两步即可。
