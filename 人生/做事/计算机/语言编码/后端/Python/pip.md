## pip网速慢

linux下,修改 ~/.pip/pip.conf 

``` ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

windows 下 ，在 用户目录(C:\Users\xx\pip) ，pip.ini 文件