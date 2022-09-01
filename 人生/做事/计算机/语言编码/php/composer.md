
## 依赖管理
   
- 安装所有依赖 composer install
- 更新所有依赖 composer update
- 下载并安装某个依赖 composer require twig/twig:~1.8  命名规范
- 安装到全局空间 composer global require phpunit/phpunit
- composer 仓库 https://packagist.org/?
  
## 组件管理
### 创建组件

厂商名和包名要唯一，我建议都使用小写。厂商名要表明所属，包名也就是组件名。

### 命名空间
组件使用的命名空间与组件的厂商名和包名无关。

### 实现组件
### 版本控制
我们最好使用语义版本方案为组件的每个版本创建标签 (tag)。
### 提交到 packagist

登录 https://packagist.org/register ，提交 github 的 Repository URL

### 使用组件

composer require 厂商名/组件名
``` php
require 'vendor/autoload.php';

$scanner= new \Oreilly\ModernPHP\Scanner();
.....

``` 

## 常用的库

| 用途说明                                                      | 备注                             |
| ------------------------------------------------------------- | -------------------------------- |
| Requests                                                      | 简单易用的HTTP请求库             |
| 轻量级配置加载类,支持多种配置格式PHP, INI, XML, JSON, and YML | 各个框架都有各自对应的配置加载类 |
| monolog/monolog                                               | 日志操作                         |
| phpmailer/phpmailer                                           | 邮件发送                         |
| opauth/opauth                                                 | PHP的多提供者身份验证框架        |
| league/csv                                                    | CSV操作类                        |
| phpunit/phpunit                                               | 它是一款轻量级的php测试框架      |
| phpoffice/phpspreadsheet                                      | excel操作类                      |
| imagine/imagine                                               | 图片处理                         |

## 库
### imagine

```php

<?php
require_once("vendor/autoload.php");
// 测试 imagine 图形库

$imagine= new Imagine\Gd\Imagine();

$size    = new Imagine\Image\Box(40, 40);

$mode    = Imagine\Image\ImageInterface::THUMBNAIL_OUTBOUND;

$imagine->open('e:\Users\Administrator\Pictures\高清图\a.jpg')
    ->thumbnail($size, $mode)
    ->save('e:\Users\Administrator\Pictures\高清图\b.jpg');
```