import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import keyword

def highlight_syntax(event=None):
    # 获取文本内容
    code = text.get("1.0", "end-1c")

    # 清除所有标记
    text.tag_remove("keyword", "1.0", "end")

    # 高亮关键字
    for word in keyword.kwlist:
        start = "1.0"
        while True:
            start = text.search(word, start, stopindex="end", nocase=True)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            text.tag_add("keyword", start, end)
            start = end

def save_file():
    # 保存文件
    filename = input("请输入文件名：")
    with open(filename, 'w') as file:
        file.write(text.get("1.0", "end-1c"))
    print(f"文件 {filename} 保存成功！")

# 创建主窗口
root = tk.Tk()
root.title("简易代码编辑器")

# 创建文本编辑框
text = scrolledtext.ScrolledText(root, width=80, height=30)
text.pack()

# 创建关键字标记
text.tag_config("keyword", foreground="blue")

# 绑定键盘事件，实现自动高亮
text.bind("<KeyRelease>", highlight_syntax)

# 创建保存按钮
save_button = tk.Button(root, text="保存", command=save_file)
save_button.pack()

# 运行主循环
root.mainloop()


# 这个简单的代码编辑器具有以下功能：

# 文本编辑：你可以在文本编辑框中输入和编辑代码。
# 代码高亮：编辑器会自动将 Python 关键字（如 if、for、while 等）高亮显示。
# 保存文件：你可以点击保存按钮，将编辑器中的代码保存到文件中。
# 请注意，这只是一个非常简化的示例，仅提供了一些基本的功能。一个完整的代码编辑器会包含更多的功能，如语法检查、自动补全、代码折叠等。如果你需要一个更复杂和完整的代码编辑器，建议使用专业的代码编辑器，如Visual Studio Code、PyCharm等，它们提供了丰富的功能和更好的用户体验。