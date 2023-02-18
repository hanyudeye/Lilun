## 几乎完整的Linux架构图   
```
 用户   应用程序（sh、vi、OpenOffice.org等）   
 模式

        复杂库（KDE、glib等）   
        简单库（opendbm、sin等）  
        C库（open、fopen、socket、exec、calloc等）   
 内核   系统中断、调用、错误等软硬件消息   
 模式
        内核（驱动程序、进程、网络、内存管理等）   
        硬件（处理器、内存、各种设备）   
```

## 用户帮助
- man
- info


(1) User commands
(2) System calls
(3) Standard library functions
(8) System/administrative commands

## 设备管理

### 磁盘管理

#### 磁盘挂载

- 查看分区 sudo fdisk -l
- 查看 UUID/type sudo blkid
- 编辑挂载文件 /etc/fstab

``` 
UUID=8A11-521D /media/MYUSBSTICK vfat defaults 0 0
UUID=E8D6B339D6B3073A /media/NTFShare ntfs defaults 0 0
UUID=d17b3219-a43d-4c38-b9cd-0ad892fa9d6e /media/Bankai ext4 defaults 0 0
```
- 重启测试
  

### 网络

``` shell
<!-- 网络开关 -->
nmcli network on/off
<!-- 无线开关 -->
nmcli radio wifi on/off
```
