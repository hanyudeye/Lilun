###
 # @Descripttion:  条件命令的使用
 # @version: 
 # @Author: hanyudeye
 # @Date: 2022-03-08 14:24:41
 # @LastEditTime: 2022-03-08 14:29:50
### 

if test -f env.sh
then 
    echo env.sh 文件存在
fi


if [ -f env.sh ]
then 
    echo env.sh 文件存在
fi


# 字符串比较
if [ "hello" = "hello" ]
then
    echo "hello=hello"
fi