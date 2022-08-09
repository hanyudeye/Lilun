### 性状 (trait)

性状是类的部分实现(即常量，属性和方法)，可以混入一个或多个现有的PHP类中。
性状有两个作用：表明类可以做什么（像是接口）；提供模块化实现（像是类）

#### 为什么使用性状
PHP是单继承的，但如果想让两个无关的类具有类似的行为，如 RetailStore(零售商店)和Car，但都要地理编码技术，在地图上显示。

性状就是用来处理这种i情况，性状能把模块化的实现方式注入多个无关的类中，还能促进代码重用。

例子如上所说，第一反映是创建 Geocodable 接口，然后在两个类中实现此接口，但编码相同，不符合DRY (不要重复你自己 ) 原则。

所以，好的方法是创建 Geocodable 性状，定义并实现地理编码相关的地方，然后在 RetailStore 和 Car中混入这个性状。这么做不会搅乱这两个类原本自然的继承层次结构。

#### 创建性状
``` php
trait Geocodable {
// 变量 
protected $address;
protected $geocoder;

protected $geocoderResult;

public function setGeocoder(\Geocoder\GeocoderInterface $geocoder){
$this->geocoder = $geocoder;
}

public function setAddress($address){
$this->address= $address;
}

public function getLatitude(){
if(isset($this->geocoderResult)===false){
$this->geocodeAddress();
}

return $this->geocoderResult->getLatitude();
}
}
```
#### 如何使用性状
PHP性状的使用方法很简单，把use MyTrait(已创建的性状名); 语句加到PHP 类的定义体中。

``` php
class MyClass{
    use MyTrait;
    // 这里是类的实现
}
```

注意: 命名空间和性状都使用 use关键字，但区别是性状导入的语句在类内，要注意。

``` php
$geocoderAdapter = new \Geocoder\HttpAdapter\CurlHttpAdapter();
$geocoder = new \Geocoder\Geocoder($geocoderAdapter);


$store = new RetailStore();
$store->setAddress('420 9th aven,New York...');
$store->setGeocoder($geocoder);

$latitude = $store->getLatitude();
$longitude= $store->getLongitude();
echo $latitude,':',$longitude;

```
警告: PHP 解释器在编译时会把性状复制粘贴到类的定义体中，但是不会处理这个操作引入的不兼容问题。如果性状假定类中有特定的属性或方法（在性状中没有定义），要确保相应的类中有对应的属性和方法。

### 生成器(generator)
与标准的PHP迭代器不同，PHP生成器不要求类实现Iterator接口，从而减轻了类的负担。生成器会根据需求计算并产出要迭代的值。这对应用的性能有重大影响。假如标准的PHP迭代器经常在内存中执行迭代操作，这要预先计算出数据集，性能低下；如果要使用特定的方式计算大量数据，对性能的影响更甚。此时，我们可以使用生成器，即时计算并产出后续值，不占用宝贵的内存资源。



### 内置的HTTP服务器
php -S localhost:4000 启动内置服务器
php -S 0.0.0.0:4000 监听局域网内所有端口，用来其它设备测试
php -S localhost:8000 -c app/config/php.ini  专属初始化配置文件加载
php -S localhost:8000 router.php  解决内置服务器不支持 .htaccess 的问题 

判断是否是内置服务器
``` php
if(php_sapi_name()=== 'cli-server'){
//PHP内置web服务器
}else{
其他服务器
}

```

## 标准 (Standards)

## 组件（Components)

使用组件就不用再使用大型框架了

组件优点:
作用单一,小型，合作，测试良好，文档完善

我们可以在 https://packagist.org 查找组件(通过口碑和下载量两种合并的方式)，[awesome php](https://github.com/ziadoz/awesome-php) 中的组件是常用的。


## Good Practices 良好实践

### 对数据进行过滤、验证和转义

未经验证的数据
- $_GET
- $_POST
- $_COOKIE
- $argv
- php://stdin
- php://input
- file_get_contents()
- 远程数据库
- 远程API
- 来自客户端的数据

数据过滤是指，转义或删除不安全的字符。在数据到达应用的存储层（如 Redis 或 MySql) 之前，一定要进行过滤。

如在评论中，插入恶意 script 标签
<script>window.location.href='http://example.com';</script>

过滤 html，使用 htmlentities()，把特殊字符(&,>等 )转换成实体。

``` php
$input = '<p><script>alert("bad");</script></p>';
echo htmlentities($input,ENT)
```

第二个参数 ENT_QUOTES，转义引号，第三个参数表示输入字符串的字符集。

警告： 别使用正则表达式函数过滤 Html，如 preg_replace()、preg_replace_all() ，写出的正则表达会很复杂，容易出错。

### SQL 查询

有时，必须根据输入数据构建SQL查询。
如：
``` php
$sql = sprintf(
'update users set password = "%s" where id = %s',
$_POST['password'],
$_GET['id']
);
```
这么做不好，如果HTTP请求如下

``` 
POST /user?id=1 HTTP/1.1
Content-Type:application/x-www-form-urlencoded

password=abc";--
```
这个 HTTP请求会把每个用户的密码都设为abc, 因为很多SQL数据库把 -- 视作注释的开头，所以会忽略后续文本

过滤电子邮件
``` php
$email = 'john@example.com';
$emailSafe=filter_var($email,FILTER_SANITIZE_EMAIL);
```

### 密码
绝对不要知道用户的密码，也不能有获取用户密码的方式，知道的越少越好，可以避免法律责任。
绝对不要约束用户的密码，如果要约束密码，建议只限制最小长度，把常用密码或基于字典创建的密码加入黑名单也是好主义
绝对不能通过电子邮件发送用户密码，而是用于改密的URL
使用 bcrypt 计算用户密码的哈希值，哈希与加密不是一回事，哈希不能解密.使用 bcrypt 最安全

### 注册用户
``` php
try{
    //验证电子邮件递质
    $email=filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL);
    if(!$email){
        throw new Exception('Invalid email');
    }

    // 验证密码
    $password = filter_input(INPUT_POST,'password');
    if(!$password || mb_strlen($password)<8>){
        throw new Exceptino('Password must contain 8+ characters');
    }

    // 创建密码的哈希值
    $passwordHash = password_hash($password,PASSWORD_DEFAULT,['cost'=>12]);
    if($passwordHash === false){
        throw new Exception("Password hash failed');
    }

    //创建用户账户
    $user = new User();
    $user->email=$email;
    $user->password_hash = $passwordHash;
    $user->save();

    // 重定向登录页面
    header('HTTP/1.1 302 Redirect');
    header('Location:/login.php);

}catch(Exception $e){
    //报告错误
    header('HTTP/1.1 400 Bad request');
    echo $e->getMessage();
}
``` 

### 登录用户

``` php
session_start();
try{
    ... 
    if(password_verify($password,$user->password_hash)===false){
        throw new Exception("Invalid password");
    }catch(Exception $e){
    header('HTTP/1.1 401 Unauthorized');
    echo $e->getMessage();
    }
}

``` 
## Hosting

## Provisioning

## Tuning

## Deployment (部署)

## Testing

## Profiling

## HHVM and hack

## Community

## Appendix

### Local Development environment

使用虚拟机的方式构建本地环境，要与发布环境一致。 docker 

### 配套代码

https://github.com/codeguy/modern-php

