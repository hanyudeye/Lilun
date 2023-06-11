
---
layout: default
toc: false
title: Linux类型的计算机管理
date:  2023-06-10T10:12:06+08:00
categories: ['技术']
---

对Linux类型的计算机进行管理

<!--more-->

文件管理
- tree  
- ls

创建目录
- mkdir 

查看文件信息
- file

adduser 添加用户
设置用户密码
passwd 管理员名称

添加到管理组
gpasswd -a 管理员名称 sudo

配置管理权限
sudo visudo 
管理员名称 ALL=(ALL:ALL) ALL

显示网络连接、路由表、接口统计、伪装连接、多播成员信息。
- netstat
- netstat -tcp

测试到目标主机的网络是否畅通
- ping 

 控制内存
- free 查看内存使用情况

 控制外部存储
- mount

 压缩打包文件
- tar 
- zip

ssh 通过网路管理计算机

用于登陆远程主机并执行命令行，默认端口22，是一种加密的传输方式。

- ssh root@192.168.1.2

修改端口配置
sudo vi /etc/ssh/sshd_config

ssh -p 端口号 管理员名称@公网IP