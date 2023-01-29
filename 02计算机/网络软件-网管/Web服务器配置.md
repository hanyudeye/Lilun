
## apache 配置 httpd.conf

``` conf 
Timeout 300 # 设定超时时间
Listen 80 #设置监听IP及端口  Listen 127.0.0.1:8080
DocumentRoot "/www"  # 设置站点根目录
```

### .htaccess 配置
- 隐藏入口文件
``` 
<IfModule mod_rewrite.c>
 RewriteEngine on
 RewriteBase /
 RewriteCond %{REQUEST_FILENAME} !-d
 RewriteCond %{REQUEST_FILENAME} !-f
 RewriteRule ^(.*)$ index.php?s=/$1 [QSA,PT,L]
</IfModule>
```


## Nginx 配置

### ng.htaccess 配置
- 隐藏入口文件

``` c 
location / {
    if (!-e $request_filename){
        rewrite  ^(.*)$  /index.php?s=$1  last;   break;
    }
}
```


## 内网穿透 natapp

### 临时域名
natapp -authtoken=e4eb817e91aeee83  

由于微信屏蔽了natapp的三级域名，所以如果需要进行微信支付或者微信小程序的联调时需要注册一个二级域名


如果用于联调微信小程序的话，则需要注册带有SSL证书的，因为微信小程序仅支持https协议。


