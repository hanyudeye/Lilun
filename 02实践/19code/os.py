# 使用 python 做一个操作系统
import os

while True:
    line = input("$ ")
    # print(line)
    #使用result接收返回值
    result=os.system(line)
    print(result)
