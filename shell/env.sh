###
 # @Descripttion: 显示环境变量
 # @version: 
 # @Author: hanyudeye
 # @Date: 2022-03-08 13:54:31
 # @LastEditTime: 2022-03-08 14:22:44
### 


echo "家目录是" $HOME
echo "命令提示符 PS1 是"  $PS1
echo "后续提示符是 PS2 是"  $PS2
echo "域分隔符是 IFS 是"  $IFS 

echo shell脚本的名字  $0      
echo  传递给脚本的参数个数  $#
echo  shell 脚本的进程号  $$ 

echo "$* 的参数是 " $*
echo "$@ 的参数是 " $@