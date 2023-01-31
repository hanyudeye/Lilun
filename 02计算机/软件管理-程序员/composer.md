
## composer 指挥家

包管理器 - 管家

下载,安装

- 1.composer.phar wget https://getcomposer.org/composer.phar
- 2.重命名composer.phar为composer mv composer.phar composer
- 3.增加可执行权限 chmod +x composer



- 安装 

```php
php composer.phar install
或
composer install
```

带自动加载文件 vendor/autoload.php

```php
require "vendor/autoload.php";
```

配置国内源

``` sh
composer config -g repo.packagist composer https://packagist.phpcomposer.com
```

composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

- 阿里云 Composer 镜像 https://mirrors.aliyun.com/composer/
- 腾讯云 Composer 镜像 https://mirrors.cloud.tencent.com/composer/



显示全局设置
```sh
composer config --list --global
```
