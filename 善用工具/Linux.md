
计算机里面，需要存放资源的存储，有资源，有工具
- 文件资源 (家具，米面，零食)
- 设备资源
- 工具资源 （运行着的工具是进程）

# 资源编辑器
- vim

# 资源管理

- 查看分区 sudo fdisk -l
- 查看 UUID/type sudo blkid
- 编辑挂载文件 /etc/fstab

``` 
UUID=8A11-521D /media/MYUSBSTICK vfat defaults 0 0
UUID=E8D6B339D6B3073A /media/NTFShare ntfs defaults 0 0
UUID=d17b3219-a43d-4c38-b9cd-0ad892fa9d6e /media/Bankai ext4 defaults 0 0
```

# 网络资源

``` shell
<!-- 网络开关 -->
nmcli network on/off
<!-- 无线开关 -->
nmcli radio wifi on/off
```
