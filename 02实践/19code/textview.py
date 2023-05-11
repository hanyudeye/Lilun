#!/usr/bin/env python
# 文本显示程序

import os
import sys

if __name__=="__main__":
    # print("参数0",sys.argv[1])
    try:
        f=open(sys.argv[1],"r")
        # show(f)
    except FileExistsError:
        print("文件不存在")
    else:
        # 显示文件
        line=f.readline()
        count=1
        while(line):
            print(line)
            line=f.readline()
            # count+=1
            # print(count)
        f.close()
    
