/*
 * @Descripttion: 读取标准输入（键盘），然后标准输出（屏幕） 
 * @version: 
 * @Author: hanyudeye
 * @Date: 2022-03-06 06:42:39
 * @LastEditTime: 2022-03-06 07:56:11
 */
#include "../include/include.h"

#define BUFFERSIZE 4096
int main(int argc, char const *argv[])
{

    int n;

    // 只能存10个字符，多的被扔掉  ,这是错误的,多的不会被扔掉，会被多次存储
    //可以用文件输入测试，不同缓存对性能的影响
    // time ./stdin-out < stdin-out > /dev/zero
    // 本机当 BUFFERSIZE为1 时，输出为
    // 0.00s user 0.01s system 97% cpu 0.010 total
    // 为10 时，输出为
    // 0.00s user 0.00s system 87% cpu 0.002 total
    // 为4096 时，输出为
    // 0.00s system 80% cpu 0.001 total
    // 所以当文件较大时，缓冲区大一些

    char buf[BUFFERSIZE];

    while ((n = read(STDIN_FILENO, buf, BUFFERSIZE)) > 0)
    {
        if (write(STDOUT_FILENO, buf, n) != n)
        {
            printf("输出错误\n");
        }
    }

    if (n < 0)
    {
        printf("读取错误\n");
    }
    else if (n == 0)
    {
        printf("ctrl D 能 产生 n==0\n");
    }

    return 0;
}
