用文字的形式 给计算机 下指令

## tree

以树形格式列出指定目录的内容，可以用于在命令行当中展示目录结构。

- -L 显示深度
- --dirsfirst 优先显示目录

## ls 

- -al 查看当前目录下的所有文件列表

## mkdir 

- -p 如果所创建的目录，父目录不存在，则相应的父目录也一起创建

## echo
输出一行文字

## file

查看文件信息

## ssh

用于登陆远程主机并执行命令行，默认端口22，是一种加密的传输方式。

- ssh root@192.168.1.2

## telnet
属于另外一种登陆远程主机的方式，默认端口为23，采用非加密的明文传输

## netstat
显示网络连接、路由表、接口统计、伪装连接、多播成员信息。

- netstat -tcp

## ping 
测试到目标主机的网络是否畅通

## free
查看内存使用情况

## mount
挂在文件系统


## tar 
打包文件夹

## 切换ip 地址
 192.168.31.100/24

wlx1cbfce955c41

要配置静态 IP 代替 DHCP，使用 vi 或 nano 编辑器编辑 netplan 配置文件并添加以下内容。

```
$ sudo vi 00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
renderer: networkd
ethernets:
ens33:
addresses:
- 192.168.1.247/24
nameservers:
addresses: [4.2.2.2, 8.8.8.8]
routes:
- to: default
via: 192.168.1.1
version: 2
```

要是上述修改生效，请使用以下 netplan 命令应用这些更改：

$ sudo netplan apply
运行以下 IP 命令查看接口上的 IP 地址：

$ ip addr show ens33
要查看默认路由，请运行：

$ ip route show
