import math
import sys
import os

# 数字处理
# 平方
# print(int(math.pow(7, 2)))

# 字符串处理
# 文字拼接处理
# print("a"+"b")


# 数组处理 (数据段，集合)
# a=[1,3,4]
# print()
# a.append([2,5])
# print(a)


# 文件处理
# f=open("./t.php")
# files=f.readlines()
# print(files)
# print(os.getcwd())


# 网络处理


# 正则表达式处理
import re

p=re.compile('ab*',re.IGNORECASE)
# print(p)

m=p.search('tempABcdef ab abc')
print(m) 
print(m.group()) 
print(m.start()) 
print(m.end()) 
print(m.span()) 