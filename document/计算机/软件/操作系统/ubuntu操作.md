## Ubuntu20.04 在休眠之后，如果网络出现了无法连接或者无法共享的各种问题，只有重启才能解决，那么以下操作可以让你不用重启电脑。

### 解决方案

**重启 network kernel modules/drivers。** 具体步骤如下：

### 查找自己的 kernel module 型号：

运行命令: `sudo lshw -C network`  
找到 `configuration：`字段中`driver=your_kernel_name`

### 重启

运行如下命令

sudo modprobe -r your_kernel_name
sudo modprobe -i your_kernel_name


需要测试
 Realtek Semiconductor
enp34s0

这是有线网卡  r8169
sudo modprobe -r  r8169
sudo modprobe -i r8169


这是无线网卡  300 找的
wlx081077a3110e

sudo modprobe -r  rtl8192cu 
sudo modprobe -i  rtl8192cu

## 为什么要使用 阿里的源？ 

因为国内的速度更快

**第一步：备份源文件：**
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup

**第二步：编辑/etc/apt/sources.list文件**

在文件最前面添加以下条目(操作前请做好相应备份)：  
vi /etc/apt/sources.list

网易163源

\# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释  
deb http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse  
deb http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse  
deb http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse  
deb http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse  
\# deb-src http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse  
\# deb-src http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse  
\# deb-src http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse  
\# deb-src http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse  
\# 预发布软件源，不建议启用  
\# deb http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse  
\# deb-src http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse

**第三步：执行更新命令：**

_sudo apt-get update  
sudo apt-get upgrade_