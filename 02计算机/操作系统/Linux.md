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