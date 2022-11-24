
## linux

![](images/2022-11-16-18-33-42.png)

### 进程

![](images/2022-11-16-18-35-16.png)

### 工作
![](images/2022-11-16-18-35-51.png)

### 资源

![](images/2022-11-16-18-36-43.png)

### 日志

![](images/2022-11-16-18-37-18.png)


### 远程登录

![](images/2022-11-17-15-57-14.png)

### 文件
![](images/2022-11-17-15-57-59.png)

```sh
ls -l  # 显示文件
chgrp [-R] 属组名 文件名  # 更改文件归属
```


### 磁盘
![](images/2022-11-17-16-00-02.png)
``` sh
df [-ahikHTm] [目录或文件名]  #查看磁盘
du [-ahskm] 文件或目录名称  # 查看磁盘用量
mkfs [-t 文件系统格式] 装置文件名 #磁盘格式化

#磁盘挂载与卸除
mount [-t 文件系统] [-L Label名] [-o 额外选项] [-n]  装置文件名  挂载点
```

### 软件包
![](images/2022-11-17-16-02-42.png)

```sh
列出所有可更新的软件清单命令：sudo apt update
列出所有已安装的包：apt list --installed
查找软件包命令： sudo apt search <keyword>
移除软件包及配置文件: sudo apt purge <package_name>
```