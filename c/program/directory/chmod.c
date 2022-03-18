/*
 * @Descripttion: 
 * @version:  改变文件的属性
 * @Author: hanyudeye
 * @Date: 2022-03-08 21:02:02
 * @LastEditTime: 2022-03-08 21:19:08
 */

#include "../include/include.h"

int main(int argc, char const *argv[])
{

    printf("需要修改文件%s 为可执行权限,请输入yes 或者no\n", argv[1]);
    char isyes[10];

    int len = scanf("%s", isyes);
    printf("%s", isyes);

    if (strcmp(isyes ,"yes")==0)
    {
        int i = chmod(argv[1], S_IXUSR|S_IRUSR|S_IWUSR);
        printf("返回结果是 %d\n", i);
    }
    else
    {
        printf("修改错误\n");
    }

    return 0;
}
