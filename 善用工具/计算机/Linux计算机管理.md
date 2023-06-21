
---
layout: default
toc: false
title: Linux类型的计算机管理
date:  2023-06-10T10:12:06+08:00
categories: ['技术']
---

对Linux类型的计算机进行管理，此计算机适合计算机工程师，不适合普通用户，普通用户适合图形化的。

<!--more-->

# 文件管理器
- tree  用树状图的形式 显示 磁盘文件  
- ls 显示当前目录下的文件 
- mkdir  创建目录
- file  查看文件信息

 压缩打包文件
- tar 
- zip


# 登陆用户管理器
- adduser 创建一个登陆用户
- passwd 设置用户密码 
- gpasswd -a 管理员名称 sudo 添加到管理组

配置管理权限
sudo visudo 
管理员名称 ALL=(ALL:ALL) ALL

# 计算机设备管理

- free 查看内存使用情况
- mount 存储挂在


# 网络管理器(计算机外交管理器)

>网络可以 获取 远程的计算机资源，就像获取本机的一样

- netstat 显示网面的计算机，网络连接、路由表、接口统计、伪装连接、多播成员信息。
- netstat -tcp
- ping  查看外面的计算机在不在线

ssh 通过网路管理计算机

用于登陆远程主机并执行命令行，默认端口22，是一种加密的传输方式。

- ssh root@192.168.1.2

修改端口配置
sudo vi /etc/ssh/sshd_config

ssh -p 端口号 管理员名称@公网IP