
# 1.检查计算机硬件是否支持WOL(wake on lan)功能。

1.1.检查主板和电源是否支持WOL
进入BIOS的Power Management Setup，设置PME Event Wake Up(这其实是一种Wake On PCI Card模式)为 Enabled。注意，有些机器可能为Wake On Lan或Wake On PCI Card。Wake On Lan模式可以在完全关机状态下唤醒，而Wake On PCI Card模式要在深度休眠状态下唤醒。造成这样的区别主要是因为主板的设计不一样，现在的计算机一般都是Wake On PCI Card模式的。

1.2.检查网卡是否支持WOL。
安装ethtool，并执行以下命令：

sudo apt-get install ethtool
sudo ethtool eth0 |grep Wake-on
如果显示结果为下面这样，就表示网卡支持WOL：

Supports Wake-on:pumbg
Wake-on : g
2.远程控制计算机进入深度休眠或完全关机状态
这里主要应用了SSH连接远程计算机，并提交命令请求来达到目的。

2.1.使用ubuntu终端登陆远程计算机
关于这一步可以参考ubuntu终端连接远程计算机

2.2.登陆远程计算机后，使用如下命令实现深度休眠或关机
#深度休眠
sudo pm-hibernate

#关机
sudo shutdown 0
3.唤醒远程计算机
3.1.准备工作
知道远程计算机的ip地址或域名和MAC地址，在路由上绑定局域网ip地址和MAC地址。如果没有静态ip，可以使用花生壳。详细操作可以google，在这里就不详述了。
在本地计算机上安装远程唤醒工具wakeonlan:
sudo apt-get install wakeonlan
3.2.唤醒远程计算机
执行下面的命令就可以唤醒远程的计算机了：

#host_address为远程计算机的域名或ip地址，mac_address为远程计算机的mac地址,mac地址是':'间隔的形式
wakeonlan -i host_address mac_address
1.检查计算机硬件是否支持WOL(wake on lan)功能。
1.1.检查主板和电源是否支持WOL
进入BIOS的Power Management Setup，设置PME Event Wake Up(这其实是一种Wake On PCI Card模式)为 Enabled。注意，有些机器可能为Wake On Lan或Wake On PCI Card。Wake On Lan模式可以在完全关机状态下唤醒，而Wake On PCI Card模式要在深度休眠状态下唤醒。造成这样的区别主要是因为主板的设计不一样，现在的计算机一般都是Wake On PCI Card模式的。

1.2.检查网卡是否支持WOL。
安装ethtool，并执行以下命令：

sudo apt-get install ethtool
sudo ethtool eth0 |grep Wake-on
如果显示结果为下面这样，就表示网卡支持WOL：

Supports Wake-on:pumbg
Wake-on : g
2.远程控制计算机进入深度休眠或完全关机状态
这里主要应用了SSH连接远程计算机，并提交命令请求来达到目的。

2.1.使用ubuntu终端登陆远程计算机
关于这一步可以参考ubuntu终端连接远程计算机

2.2.登陆远程计算机后，使用如下命令实现深度休眠或关机
#深度休眠
sudo pm-hibernate

#关机
sudo shutdown 0
3.唤醒远程计算机
3.1.准备工作
知道远程计算机的ip地址或域名和MAC地址，在路由上绑定局域网ip地址和MAC地址。如果没有静态ip，可以使用花生壳。详细操作可以google，在这里就不详述了。
在本地计算机上安装远程唤醒工具wakeonlan:
sudo apt-get install wakeonlan
3.2.唤醒远程计算机
执行下面的命令就可以唤醒远程的计算机了：

#host_address为远程计算机的域名或ip地址，mac_address为远程计算机的mac地址,mac地址是':'间隔的形式
wakeonlan -i host_address mac_address