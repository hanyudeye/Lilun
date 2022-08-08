
### HTTP
#### POST 交流方式 
##### application/x-www-form-urlencoded  (原生协议)
```
POST http://www.example.com HTTP/1.1
Content-Type: application/x-www-form-urlencoded;charset=utf-8

title=test&sub%5B%5D=1&sub%5B%5D=2&sub%5B%5D=3
```
数据按照 key1=val1&key2=val2 的方式进行编码，key 和 val 都进行了 URL 转码。大部分服务端语言都对这种方式有很好的支持。例如 PHP 中，_POST['sub'] 可以得到 sub 数组

##### multipart/form-data (原生)
> 表单上传文件时，必须让 form 的 enctyped 等于这个值

``` 
POST http://www.example.com HTTP/1.1
Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryrGKCBY7qhFd3TrwA

------WebKitFormBoundaryrGKCBY7qhFd3TrwA
Content-Disposition: form-data; name="text"

------WebKitFormBoundaryrGKCBY7qhFd3TrwA
Content-Disposition: form-data; name="file"; filename="chrome.png"
Content-Type: image/png

PNG ... content of chrome.png ...
------WebKitFormBoundaryrGKCBY7qhFd3TrwA--
```

##### application/json
> 使用 JSON.stringify 系列化后的 json 字符串

```
POST http://www.example.com HTTP/1.1
Content-Type: application/json;charset=utf-8

{"title":"test","sub":[1,2,3]}
```

##### text/xml (使用较少)

``` 
POST http://www.example.com HTTP/1.1
Content-Type: text/xml

<!--?xml version="1.0"?-->
<methodcall>
    <methodname>examples.getStateName</methodname>
    <params>
        <param>
            <value><i4>41</i4></value>

    </params>
</methodcall>
```
