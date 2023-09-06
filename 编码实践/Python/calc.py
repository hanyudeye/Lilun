# 简单的计算器：开发一个基本的计算器应用程序，可以执行基本的数学运算，如加法、减法、乘法和除法。

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "除数不能为零"

def calculator():
    print("欢迎使用计算器！")
    print("请选择操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("0. 退出")

    while True:
        choice = input("请输入操作编号：")

        if choice == "0":
            print("感谢使用计算器，再见！")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("无效的操作编号，请重新输入。")
            continue

        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))

        if choice == "1":
            result = add(num1, num2)
            print(f"结果：{result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"结果：{result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"结果：{result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"结果：{result}")

        print()

# 调用 calculator() 函数来运行计算器应用程序
calculator()
