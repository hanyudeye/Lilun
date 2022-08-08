---
title: PHP 程序设计
---


## 为什么要设计命名空间？
因为计算机中的内容太多，就像命令太多一样，需要更多不同的名字约束。

namespace Symfony\Component\HttpFoundation; 

>自动导入命名对象
require_once '/vendor/autoload.php';
> 手动导入命名对象
require_once "库文件";

>使用别名来简化对象的引用
use Symfony\Component\HttpFoundation\Response as Res;


## 为什么要有类？

类的作用和文件作用一样，是为了编程时，相关东西放一起，好找，为了减少杂乱

> 定义抽象类 
``` php
 abstract class Animal {
   public $name;
   abstract public function eat($food);
 }
```

> 实现类
```php
     class Whale extends Animal {
       public function __construct() {
         $this->name = "Whale";
       }
       public function eat($food) {
         echo $this->name . " eat " . $food . ".\n";
       }
     }
```

### 定义接口来被其它类继承

``` php 
       interface IAction {
           public function eat($food);
           public function swim();
       }
       class Whale implements IAction {
           echo "Whale eat " . $food . "\n.";
         }
         public swim() {
           echo "Whale is swimming.\n";
         }
       }
```

## 函数

### 类型检查
> 检查对象的类型

 - 获取变量类型 gettype()
 - 设置变量类型 settype()
 - 判断变量是否是数字类型  is_numeric()
 - 判断变量是否是布尔类型 is_bool()
 - is_float(), is_double，is_real()
 - is_int() , is_integer()
 - is_string()
 - is_object()    
 - is_array()     
 - is_null()      

 >检查变量状态
 - 判断变量是否已经声明 isset()
 - 销毁变量 unset()
 - 判断变量是否声明，或者变量值是否为空或 0  empty() 

### 类型转换
- 变量转浮点数 doubleval ，floatval
- 变量转整数  intval
- 变量转字符串  strval

### 日期 date

| 时间格式化的方式 | 说明                                                 |
|------------------+------------------------------------------------------|
| Y                | 4 位数字年，y为 2 位数字，如 99 即 1999 年                  |
| m                | 数字月份，前面有前导 0，如 01。n 为无前导 0 数字月份     |
| F                | 月份，完整的文本格式，例如 January 或者 March        |
| M                | 三个字母缩写表示的月份，例如 Jan 或者 Mar            |
| d                | 月份中的第几天，前面有前导 0，如 03。j 为无前导 0 的天数 |
| w                | 星期中的第几天，以数字表示，0表示星期天              |
| z                | 年份中的第几天，范围 0-366                            |
| W                | 年份中的第几周，如第 32 周                             |
| H                | 24 小时格式，有前导 0，h 为 12 小时格式                   |
| G                | 24 小时格式，无前导 0，g 为对应 12 小时格式               |
| i                | 分钟格式，有前导 0                                    |
| s                | 秒格式，有前导 0                                      |
| A                | 大写上下午，如 AM，a 为小写                            |

- strtotime 字符串转时间

### 目录  Directory 

| 函数        | 描述                               |
|-------------+------------------------------------|
| chdir()     | 改变当前的目录。                   |
| chroot()    | 改变根目录。                       |
| closedir()  | 关闭目录句柄。                     |
| dir()       | 返回 Directory 类的实例。          |
| getcwd()    | 返回当前工作目录。                 |
| opendir()   | 打开目录句柄。                     |
| readdir()   | 返回目录句柄中的条目。             |
| scandir()   | 返回指定目录中的文件和目录的数组。 |

### 文件系统 Filesystem

| 函数                  | 描述                                                            |
|-----------------------+-----------------------------------------------------------------|
| basename()            | 返回路径中的文件名部分。                                        |
| chgrp()               | 改变文件组。                                                    |
| chmod()               | 改变文件模式。                                                  |
| chown()               | 改变文件所有者。                                                |
| clearstatcache()      | 清除文件状态缓存。                                              |
| copy()                | 复制文件。                                                      |
| delete()              | 参见 unlink() 或 unset()                                        |
| dirname()             | 返回路径中的目录名称部分。                                      |
| disk_free_space()     | 返回目录的可用空间。                                            |
| disk_total_space()    | 返回一个目录的磁盘总容量。                                      |
| diskfreespace()       | disk_free_space() 的别名。                                      |
| fclose()              | 关闭打开的文件。                                                |
| feof()                | 测试文件指针是否到了文件末尾。                                  |
| fflush()              | 向打开的文件刷新缓冲输出。                                      |
| fgetc()               | 从打开的文件中返回字符。                                        |
| fgetcsv()             | 从打开的文件中解析一行，校验 CSV 字段。                         |
| fgets()               | 从打开的文件中返回一行。                                        |
| fgetss()              | 从打开的文件中返回一行，并过滤掉 HTML 和 PHP 标签。             |
| file()                | 把文件读入一个数组中。                                          |
| file_exists()         | 检查文件或目录是否存在。                                        |
| file_get_contents()   | 把文件读入字符串。                                              |
| file_put_contents()   | 把字符串写入文件。                                              |
| fileatime()           | 返回文件的上次访问时间。                                        |
| filectime()           | 返回文件的上次修改时间。                                        |
| filegroup()           | 返回文件的组 ID。                                               |
| fileinode()           | 返回文件的 inode 编号。                                         |
| filemtime()           | 返回文件内容的上次修改时间。                                    |
| fileowner()           | 返回文件的用户 ID （所有者）。                                  |
| fileperms()           | 返回文件的权限。                                                |
| filesize()            | 返回文件大小。                                                  |
| filetype()            | 返回文件类型。                                                  |
| flock()               | 锁定或释放文件。                                                |
| fnmatch()             | 根据指定的模式来匹配文件名或字符串。                            |
| fopen()               | 打开一个文件或 URL。                                            |
| fputcsv()             | 把行格式化为 CSV 并写入一个打开的文件中。                       |
| fputs()               | fwrite() 的别名。                                               |
| fread()               | 读取打开的文件。                                                |
| fscanf()              | 根据指定的格式对输入进行解析。                                  |
| fseek()               | 在打开的文件中定位。                                            |
| fstat()               | 返回关于一个打开的文件的信息。                                  |
| ftell()               | 返回在打开文件中的当前位置。                                    |
| ftruncate()           | 把打开文件截断到指定的长度。                                    |
| fwrite()              | 写入打开的文件。                                                |
| glob()                | 返回一个包含匹配指定模式的文件名/目录的数组。                   |
| is_dir()              | 判断文件是否是一个目录。                                        |
| is_executable()       | 判断文件是否可执行。                                            |
| is_file()             | 判断文件是否是常规的文件。                                      |
| is_link()             | 判断文件是否是连接。                                            |
| is_readable()         | 判断文件是否可读。                                              |
| is_uploaded_file()    | 判断文件是否是通过 HTTP POST 上传的。                           |
| is_writable()         | 判断文件是否可写。                                              |
| is_writeable()        | is_writable() 的别名。                                          |
| lchgrp()              | 改变符号连接的组所有权。                                        |
| lchown()              | 改变符号连接的用户所有权。                                      |
| link()                | 创建一个硬连接。                                                |
| linkinfo()       | 返回有关一个硬连接的信息。                                      |
| lstat()               | 返回关于文件或符号连接的信息。                                  |
| mkdir()               | 创建目录。                                                      |
| move_uploaded_file()  | 把上传的文件移动到新位置。                                      |
| parse_ini_file()      | 解析一个配置文件。                                              |
| parse_ini_string()    | 解析一个配置字符串。                                            |
| pathinfo()            | 返回关于文件路径的信息。                                        |
| pclose()              | 关闭由 popen() 打开的进程。                                     |
| popen()               | 打开一个进程。                                                  |
| readfile()            | 读取一个文件，并写入到输出缓冲。                                |
| readlink()            | 返回符号连接的目标。                                            |
| realpath()            | 返回绝对路径名。                                                |
| realpath_cache_get()  | 返回高速缓存条目。                                              |
| realpath_cache_size() | 返回高速缓存大小。                                              |
| rename()              | 重命名文件或目录。                                              |
| rewind()              | 倒回文件指针的位置。                                            |
| rmdir()               | 删除空的目录。                                                  |
| set_file_buffer()     | 设置已打开文件的缓冲大小。                                      |
| stat()                | 返回关于文件的信息。                                            |
| symlink()             | 创建符号连接。                                                  |
| tempnam()             | 创建唯一的临时文件。                                            |
| tmpfile()             | 创建唯一的临时文件。                                            |
| touch()               | 设置文件的访问和修改时间。                                      |
| umask()               | 改变文件的文件权限。                                            |
| unlink()              | 删除文件。                                                      |

### HTTP 

| 函数           | 描述                                                |
|----------------+-----------------------------------------------------|
| header()       | 向客户端发送原始的 HTTP 报头。                      |
| headers_list() | 返回已发送的（或待发送的）响应头部的一个列表。      |
| headers_sent() | 检查 HTTP 报头是否发送/已发送到何处。               |
| setcookie()    | 向客户端发送一个 HTTP cookie。                      |
| setrawcookie() | 不对 cookie 值进行 URL 编码，发送一个 HTTP cookie。 |

- setcookie("user", "runoob", time()+3600);
- setcookie(name, value, expire, path, domain);


```php
// Redirect to login page
header('HTTP/1.1 302 Redirect');
header('Location: /login.php');
header('HTTP/1.1 400 Bad request');
 ```

跨域问题

允许单个域名访问
header('Access-Control-Allow-Origin:http://client.runoob.com');

允许多个域名访问
```php
$origin = isset($_SERVER['HTTP_ORIGIN'])? $_SERVER['HTTP_ORIGIN'] : '';  
  
$allow_origin = array(  
    'http://client1.runoob.com',  
    'http://client2.runoob.com'  
);  
  
if(in_array($origin, $allow_origin)){  
    header('Access-Control-Allow-Origin:'.$origin);       
} 
``` 

允许所有域名访问
header('Access-Control-Allow-Origin:#'); 


### Misc 杂项 

| 函数                   | 描述                                          |
|------------------------+-----------------------------------------------|
| connection_aborted()   | 检查是否断开客户机。                          |
| connection_status()    | 返回当前的连接状态。                          |
| usleep()               | 延迟代码执行若干微秒。                        |

### String 

| trim()                       | 移除字符串两侧的空白字符和其他字符。                              |
| ucfirst()                    | 把字符串中的首字符转换为大写。                                    |

### 获取 WEB 信息
#### 服务器信息 $_SERVER 
- DOCUMENT_ROOT
#### 表单信息
- $_GET
- $_POST
- $_REQUEST ($_GET 与 $_POST 的合集)
- $_FILES 文件信息，包含 (name,type,tmp_name,error,size) 
- $_COOKIE 
- $_SESSION session 
会话信息是临时的，在用户离开网站后将被删除设置或获取 Session 都要先 执行 session_start();

#### session
php 中的 session 默认有效期是 1440秒(24分钟)

修改session时间, php.ini
1. session.use_cookies =1  # 利用 cookie来传递sessionid
2. session.cookie_lifetime = 999999999 # 这个代表 sessionid 在客户端存储的时间，默认为0 (可以设置大的数值)
3. session.gc_maxlifetime=9999999  # 这个 session表示在服务端存储的时间，可以设大点


```php
session_start();
$_SESSION['count']; //注册 session变量 count
isset($PHPSESSID)?session_id($PHPSESSID):$PHPSESSID=session_id();
// 如果设置了$PHPSESSID，就将SessionID赋值为$PHPSESSID，否则生成SessionID 
$_SESSION['count']++; // 变量count加1
setcookie('PHPSESSID', $PHPSESSID, time()+3156000); // 储存SessionID到Cookie中
echo $count; // 显示Session变量count的值 
```

### 显示错误

``` php
ini_set("display_errors","On");
error_reporting(E_ALL); 
```

### 验证

#### 验证 Email 

```php
$input = 'john@example.com';
$isEmail = filter_var($input, FILTER_VALIDATE_EMAIL); 
if ($isEmail !== false) {
    echo "Success"; 
}else{
    echo "Fail"; 
}
```

### 缓存
#### redis 

##### php.ini 配置

``` config
[redis]
extension = redis.so
```

##### 连接到 Redis 服务器 

``` php
    //Connecting to Redis server on localhost 
    $redis = new Redis(); 
    $redis->connect('127.0.0.1', 6379); 
    echo "Connection to server sucessfully"; 
    //check whether server is running or not 
    echo "Server is running: ".$redis->ping(); 
```

##### $Redis PHP 字符串示例

``` php
    //Connecting to Redis server on localhost 
    $redis = new Redis(); 
    $redis->connect('127.0.0.1', 6379); 
    echo "Connection to server sucessfully"; 
    //set the data in redis string 
    $redis->set("tutorial-name", "Redis tutorial"); 
    // Get the stored data and print it 
    echo "Stored string in redis:: " .$redis→get("tutorial-name"); 
```

##### Redis php 列表示例

``` php
    //Connecting to Redis server on localhost 
    $redis = new Redis(); 
    $redis->connect('127.0.0.1', 6379); 
    echo "Connection to server sucessfully"; 
    //store data in redis list 
    $redis->lpush("tutorial-list", "Redis"); 
    $redis->lpush("tutorial-list", "Mongodb"); 
    $redis->lpush("tutorial-list", "Mysql");  

    // Get the stored data and print it 
    $arList = $redis->lrange("tutorial-list", 0 ,5); 
    echo "Stored string in redis:: "; 
    print_r($arList); 
```

### 日期和时间

```php
$raw = '22. 11. 1968';
$start = DateTime::createFromFormat('d. m. Y', $raw);
echo 'Start date: ' . $start->format('Y-m-d') . "\n";
``` 


## 服务器配置
### php.ini
```
 error_reporting = E_ALL &~E_NOTICE &~E_STRICT
 display_errors= On
 default_charset="utf-8"
 extension_dir="./ext"
 file_uploads=On
 upload_max_filesize=2M
 session.save_path ="/tmp"
 session.gc_maxlifetime=1440   Session 过期时间
```

