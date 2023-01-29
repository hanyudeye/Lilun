## 配置 /etc/php/phpversion/php.ini
``` cnf
error_reporting = E_ALL & ~E_NOTICE & ~E_STRICT
display_errors = On
file_uploads = On
uploads_max_filesize = 10M
session.save_path = "/tmp"
session.auto_start = 0
session.gc_maxlifetime = 1440 # session 过期时间，秒为单位
```

