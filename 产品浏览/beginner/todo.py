
# 1. To-Do List 应用程序：创建一个简单的待办事项列表应用程序，允许用户添加、删除和标记完成任务。

# 1. 打开~/administrator/.todo文件，显示

# 接收输入，
# 2. d 命令
# 2.a 命令


# 用python做一个命令行 待办事项列表应用程序 ，允许用户添加、删除和标记完成任务，读取 用户目录下 .todo文件，a命令添加，d 命令删除。

import os

TODO_FILE = os.path.expanduser("~/.todo")

def display_tasks():
    # 隐藏打印文件
    # print(TODO_FILE)
    if not os.path.exists(TODO_FILE):
        return

    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
        if tasks:
            print("待办事项列表：")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.strip()}")
        else:
            print("待办事项列表为空。")

# 清除屏幕
def clear_screen():
    if os.name == "nt":
        os.system("cls")  # for Windows
    else:
        os.system("clear")  # for Unix/Linux/MacOS

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(f"{task}\n")
    print(f"已添加任务：{task}")

def delete_task(task_number):
    if not os.path.exists(TODO_FILE):
        return

    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("无效的任务编号。")
        return

    deleted_task = tasks.pop(task_number - 1)

    with open(TODO_FILE, "w") as file:
        file.writelines(tasks)

    print(f"已删除任务：{deleted_task.strip()}")

def main():
    while True:
        clear_screen()
        display_tasks()
        # print("命令：\n  a 添加任务\n  d 删除任务\n  q 退出")
        command = input("请输入命令：").lower()

        if command == "q":
            break
        elif command == "a":
            task = input("请输入任务：")
            add_task(task)
        elif command == "d":
            task_number = int(input("请输入要删除的任务编号："))
            delete_task(task_number)
        else:
            print("无效的命令。")

if __name__ == "__main__":
    main()


# 这段代码首先定义了一个常量TODO_FILE，用于存储待办事项的文件路径。然后，它定义了几个函数：display_tasks()用于显示待办事项列表，add_task(task)用于添加任务，delete_task(task_number)用于删除任务。

# 在main()函数中，程序会循环显示待办事项列表并等待用户输入命令。用户可以输入a来添加任务，输入d来删除任务，输入q来退出程序。

# 请注意，这只是一个简单的示例代码，没有进行错误处理和输入验证。在实际应用中，你可能需要添加更多的错误处理和输入验证来提高程序的健壮性。