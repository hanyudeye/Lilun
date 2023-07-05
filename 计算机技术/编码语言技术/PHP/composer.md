---
title: composer
permalink: composer.html
theme: jekyll-theme-cayman
---

composer 指挥家,用于安装和管理 PHP 包的工具

引用包，引用一个自动加载包即可
```php
require "vendor/autoload.php";
```

配置国内源

``` sh
composer config -g repo.packagist composer https://packagist.phpcomposer.com
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```
- 阿里云 Composer 镜像 https://mirrors.aliyun.com/composer/
- 腾讯云 Composer 镜像 https://mirrors.cloud.tencent.com/composer/

显示全局设置
```sh
composer config --list --global
```

- 安装包 require