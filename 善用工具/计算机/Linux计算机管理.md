---
layout: default
toc: false
title: Linux计算机家的管理
date:  2023-06-10T10:12:06+08:00
categories: ['技术']
---

用Linux 管理计算机，就像用 人管理家一样
<!--more-->

- 关闭机器  shutdown(睡觉去吧)
- 重启机器  reboot(起床干事情啦)
- 显示，配置 设备信息，系统信息 ls /dev(报上自己的大名，手脚，眼睛，耳朵)
- 显示或配置 文件信息 ls makefile  (给我讲各种故事呀，知识呀)
- 获取文件  wget ，chrome -get 
- 查看外面的人在不在  ping 
- 查找知识 find grep (局部信息查找)
- 查看谁在干活 ,任务管理  ps,top
- 到别人家里去干活  ssh+别人家地址
- 把东西压扁打包  tar  zip
- 家里多请几个家人  adduser

配置管理权限
sudo visudo 
管理员名称 ALL=(ALL:ALL) ALL

用于登陆远程主机并执行命令行，默认端口22，是一种加密的传输方式。
- ssh root@192.168.1.2
修改端口配置
sudo vi /etc/ssh/sshd_config

ssh -p 端口号 管理员名称@公网IP