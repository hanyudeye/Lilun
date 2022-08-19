用户名 admin  密码 hxVMq3vgQRAf0aua)M
https://www.yiibai.com/wordpress/wordpress_reading_setting.html#article-start

## 为什么需要 wordpress ? 
wordpress 是一个网站内容发布程序，使用简单，不用开发代码就可以使用。而且界面设计是拖动式的，方便操作。


## 安装
1. 下载 wordpress
2. 创建数据库
3. 安装向导安装  wp-admin/install.php

- 更新 wp-admin/update-core.php

## 仪表盘 (管理后台)


## Wordpress常规设置
点击 设置 -> 常规

可以设置站点标题，副标题，站点地址，邮箱

WordPress地址(URL): 这是WordPress的目录的URL，所有核心应用程序文件都存在这里。

## Wordpress撰写设置
## Wordpress阅读设置
> 阅读设置用于设置相关前端页面的内容

## 讨论
设置>讨论中去掉显示头像的勾选


# 定制
安装主题  astra
安装插件  elementor


# 编码
默认的编码整理方式为 utf8mb4_unicode_520_ci，但是 MySQL 5.5 及以下版本的数据库，不支持 utf8mb4_unicode_520_ci，所以无法导入。

处理的办法，就是使用 sublime text 等代码编辑器，打开 .sql 数据库，然后批量查找替换所有的

搜索：utf8mb4_unicode_520_ci
替换为：utf8mb4_unicode_ci


如果还会出现错误提示，尝试检查 WordPress 网站根目录下的配置文件 wp-config.php ，更改数据表默认文字编码，把里面的
define(‘DB_CHARSET’, ‘utf8mb4’);
改成：
define(‘DB_CHARSET’, ‘utf8’);

## 禁用google 字体插件
Disable Google Fonts


## 加载elementor时出现问题_Elementor插件无法编辑/加载/空白页 提示“wp-json/elementor/v1/globals”404解决办法

1、办法1：更改固定链接类型

进入WordPress后台，选择设置-固定链接

将固定链接类型改为朴素即可

可以正常加载页面了

2、办法2：添加伪静态规则

因为虾皮路是在本地测试，因此出现这个链接问题，如果不希望改动固定链接为朴素的话，可以查看自己的伪静态规则是否正确，比如Nginx的伪静态规则location /{

rewrite ^(.*)/equip(d+).html$ $1/index.php?m=content&c=index&a=lists&catid=$2 last;

}

或者在htaccess文件中配置rewrite规则rewrite ^/content/list/([0-9]+).html$ /content/list.php?id=$1 last;
