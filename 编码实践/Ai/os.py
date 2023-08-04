import os

def clear_screen():
    # 清除屏幕
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    # 显示菜单选项
    print("欢迎使用简易操作系统！")
    print("1. 查看文件列表")
    print("2. 创建文件")
    print("3. 删除文件")
    print("4. 退出")

def list_files():
    # 查看当前目录下的文件列表
    files = os.listdir('.')
    for file in files:
        print(file)

def create_file():
    # 创建新文件
    filename = input("请输入文件名：")
    with open(filename, 'w') as file:
        pass
    print(f"文件 {filename} 创建成功！")

def delete_file():
    # 删除文件
    filename = input("请输入要删除的文件名：")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"文件 {filename} 删除成功！")
    else:
        print(f"文件 {filename} 不存在！")

# 主程序
def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("请输入选项：")
        
        if choice == '1':
            clear_screen()
            list_files()
            input("按 Enter 返回菜单...")
        elif choice == '2':
            clear_screen()
            create_file()
            input("按 Enter 返回菜单...")
        elif choice == '3':
            clear_screen()
            delete_file()
            input("按 Enter 返回菜单...")
        elif choice == '4':
            clear_screen()
            print("谢谢使用，再见！")
            break
        else:
            print("无效的选项，请重新输入！")

if __name__ == '__main__':
    main()

# 这个简单的操作系统提供了以下功能：

# 1. 查看文件列表：显示当前目录下的文件列表。
# 2. 创建文件：根据用户输入的文件名，在当前目录下创建一个空文件。
# 3. 删除文件：根据用户输入的文件名，删除当前目录下的指定文件。
# 4. 退出：退出操作系统。

# 请注意，这只是一个非常简化的示例，仅提供了一些基本的文件操作功能。一个完整的操作系统会包含更多的功能，如文件夹管理、进程管理、用户权限等。如果你需要一个更复杂和完整的操作系统，建议学习更深入的计算机科学知识，或者使用现有的操作系统。