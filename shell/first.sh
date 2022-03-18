###
 # @Descripttion:  这个脚本查找目录中包含 FUCK 字符串的文件，打印文件名
 # @version: 
 # @Author: hanyudeye
 # @Date: 2022-03-08 07:35:09
 # @LastEditTime: 2022-03-08 07:46:31
### 

#!/bin/sh

for file in *
do
    if grep -q FUCK $file
    # if false
    then 
        echo $file."文件包含FUCK内容"
    fi
done

exit 0