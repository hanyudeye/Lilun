# 骰子模拟器.py
# 目的:创建一个程序来模拟掷骰子
# 提示:当用户询问时，使用random模块生成一个1到6之间的数字
import random
# # for i in range(1,50):
# print("您骰的子是：")
# print(random.randrange(1,7))

# randint  与 randrange 的差别是 , randint 包含边界，而 randrange 不包含边界
while int(input("输入1继续，输入0退出")):
    print(random.randint(1,6))
