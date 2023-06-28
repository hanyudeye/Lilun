---
layout: default
toc: false
title: python程序设计
date:  2023-06-20T14:49:57+08:00
categories: ['技术','编程语言']
---

# 对象

程序提供的可以直接处理的东西，如 文字，数字，计算机设备，环境信息等基础的东西和自己创建的或第三方扩展的东西。

## 对象转换
不同的对象，在一定程度可以转换，但可能会失去精度

- set(s)  转集合(无重复，排序随机)
- dict(d) d 必须是一个序列 (key,value)元组。
- frozenset(s)  转换为不可变集合
- chr(x) 将一个整数转换为一个字符
- ord(c) 将一个字符转换为它的整数值 (与上面互逆)
- unichr(x) 将一个整数转换为 Unicode 字符
- hex(x) 将一个整数转换为一个十六进制字符串
- oct(x) 将一个整数转换为一个八进制字符串

# 对象库

当前所创造的可以直接使用的对象

## 系统对象

    - 显示模块搜索路径  sys.path
    - 显示加载的模块 print(sys.modules)
    - 路径合理化 os.path.normpath
    - 绝对路径 abspath
    - 运行程序 os.system('python helloshell.py')
    - 把进程赋予变量 output = os.popen('python helloshell.py').read()
    - 环境变量 os.environ                                                                 
    - 运行程序 os.system, os.popen, os.execv, os.spawnv                                  
    - 进程处理  os.fork, os.pipe, os.waitpid, os.kill                                    
    - 文件描述  os.open, os.read, os.write                                              
    - 文件处理 os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir                    
    - 管理员工具 os.getcwd, os.chdir, os.chmod, os.getpid, os.listdir, os.access       
    - 移植工具 os.sep, os.pathsep, os.curdir, os.path.split, os.path.join  
    - 路径名称工具 os.path.exists('path'), os.path.isdir('path'), os.path.getsize('path')     

## 数学运算
### math
    - pi
    - floor 地板
    - trunc 截断
### random
    - random
## 字符串和文本处理 
### odecs 
# 进程  
### 创建进程
    Process([group [, target [, name [, args [, kwargs]]]]])
    target 表示调用对象
    args 表示调用对象的位置参数元组
    kwargs 表示调用对象的字典
    name 为别名
    group 实质上不使用

    下面看一个创建函数并将其作为多个进程的例子：

    ``` python
      #!/usr/bin/env python3
      import multiprocessing
      import time


      def worker(interval, name):
          print(name + '【start】')
          time.sleep(interval)
          print(name + '【end】')


      if __name__ == "__main__":
          p1 = multiprocessing.Process(target=worker, args=(2, '两点水 1'))
          p2 = multiprocessing.Process(target=worker, args=(3, '两点水 2'))
          p3 = multiprocessing.Process(target=worker, args=(4, '两点水 3'))

          p1.start()
          p2.start()
          p3.start()

          print("The number of CPU is:" + str(multiprocessing.cpu_count()))
          for p in multiprocessing.active_children():
              print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
              print("END!!!!!!!!!!!!!!!!!")
    ```

### 把进程创建成类
    当然我们也可以把进程创建成一个类，如下面的例子，当进程 p 调用 start() 时，自
    动调用 run() 方法。

    ``` python
      import multiprocessing
      import time


      class ClockProcess(multiprocessing.Process):
          def __init__(self, interval):
              multiprocessing.Process.__init__(self)
              self.interval = interval

          def run(self):
              n = 5
              while n > 0:
                  print("当前时间: {0}".format(time.ctime()))
                  time.sleep(self.interval)
                  n -= 1

      if __name__ == '__main__':
          p = ClockProcess(3)
          p.start()
    ```

### daemon 属性

    想知道 daemon 属性有什么用，看下下面两个例子吧，一个加了 daemon 属性，一个没有加，对比输出的结果：

    没有加 deamon 属性的例子：

    ``` python
      import multiprocessing
      import time


      def worker(interval):
          print('工作开始时间：{0}'.format(time.ctime()))
          time.sleep(interval)
          print('工作结果时间：{0}'.format(time.ctime()))


      if __name__ == '__main__':
          p = multiprocessing.Process(target=worker, args=(3,))
          p.start()
          print('【EMD】')

    ```
    输出结果：

    ```txt
    【EMD】
    工作开始时间：Mon Oct  9 17:47:06 2017
    工作结果时间：Mon Oct  9 17:47:09 2017
    ```

    在上面示例中，进程 p 添加 daemon 属性：

    ```python

    import multiprocessing
    import time


    def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


    if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    print('【EMD】')
    ```

    输出结果：

    ```txt
    【EMD】
    ```


    根据输出结果可见，如果在子进程中添加了 daemon 属性，那么当主进程结束的时候，子
    进程也会跟着结束。所以没有打印子进程的信息。
## 网络编程与套接字
### 网路编程基础 
### asynchat
### asynncore
### select
### socket
#### 地址族
#### 套接字类型
#### 寻址
#### 函数
#### 异常
#### 示例
### ssl
### SocketServer
## Internet 编程
### ftplib
### http
#### http.client 
#### http.server
#### http.cookie
#### http.cookiejar
### smtplib
### urllib
### xmlrpc
## Web 编程
### cgi
### cgitb
### wsgiref
### webbrowser
## Internet 数据处理与编码
### base64
### binascii
### csv
### email
### hashlib
### hmac
### HtMLParser
### json
### mimetypes
### quopri
### xml
## 其它库
### Python 服务
### 国际化
### 多媒体
## 扩展与嵌入
### 扩展模块
# 工具
## 虚拟环境 virtualenv 管理包
   环境，就是用某个环境的工具执行代码喽，激活了环境记得关闭此环境哦
    
### 创建虚拟环境
    创建 env 环境目录   virtualenv env
    创建目录，并选用 python3 的解释器 virtualenv -p /usr/local/bin/python3 venv
### 启动虚拟环境 source ./bin/activate
    Virtualenv 附带有 pip 安装工具，因此需要安装的 packages 可以直接运行：
### 退出虚拟环境 deactivate
### 删除虚拟环境 rm -rf 
### 虚拟环境管理工具 Virtualenvwrapper 
#### 创建虚拟机 mkvirtualenv env
#### 列出虚拟环境列表 workon 或者 lsvirtualenv
#### 启动/切换虚拟环境 workon [virtual-name]
#### 删除虚拟环境 rmvirtualenv  [virtual-name]
#### 离开虚拟环境 deactivate
## 版本管理 pyenv,管理 python 版本

   常用命令 
   pyenv versions – 查看系统当前安装的 python 列表
   pyenv version – 查看系统当前使用的 python 版本
   pyenv install -v 3.5.3 – 安装 python
   pyenv uninstall 2.7.13 – 卸载 python
   pyenv rehash – 为所有已安装的可执行文件（如：~/.pyenv/versions/bin/）创建 shims， 因此每当你增删了 Python 版本或带有可执行文件的包（如 pip）以后，都应该执行一次本命令）
   
   版本切换
   pyenv global 3.5.3 – 设置全局的 Python 版本，通过将版本号写入~/.pyenv/version 文件的方式
   pyenv local 2.7.13 – 设置面向程序的本地版本，通过将版本号写入当前目录下的.python-version 文件的方式。 通过这种方式设置的 Python 版本优先级较 global 高。
   pyenv shell 2.7.13 - 设置面向 shell 的 Python 版本，通过设置当前 shell 的 PYENV_VERSION 环境变量的方式
   优先级: shell > local > global

   卸载 pyenv
   禁用 pyenv 很简单，只需要在~/.bash_profile 中的 pyenv init 那行删了即可。
   完全移除 pyenv，先执行上面第 1 步，然后删了 pyenv 的根目录: rm -rf $(pyenv root)
   插件 pyenv-virtualenv
   
   安装插件    官网地址: https://github.com/pyenv/pyenv-virtualenv

   使用自动安装 pyenv 后，它会自动安装部分插件，通过 pyenv-virtualenv 插件可以很好的和 virtualenv 结合
   另外，一个可选配置是在~/.bash_profile 最后添加:

   eval "$(pyenv virtualenv-init -)"
   
   可以实现自动激活虚拟环境，这个特性非常有用建议都加上。

   创建虚拟环境: pyenv virtualenv 2.7.13 virtual-env-2.7.13，默认使用当前环境 python 版本。 在文件夹$(pyenv root)/versions/my-virtual-env-2.7.13 中创建一个基于 Python 2.7.13 的虚拟环境。
   列出虚拟环境: pyenv virtualenvs，对每个 virtualenv 显示 2 个, 短的只是个链接，那个#表示当前激活的。
   激活虚拟环境: pyenv activate virtual-env-2.7.13
   退出虚拟环境: pyenv deactivate
   删除虚拟环境: pyenv uninstall virtual-env-2.7.13
   
   如果 eval "$(pyenv virtualenv-init -)"写在你的 shell 配置中(比如上面
   的~/.bash_profile), 那么当 pyenv-virtualenv 进入/离开某个含有.python-version
   目录时会自动激活/退出虚拟环境。
   
   场景使用流程:

   # 先创建一个虚拟环境
   pyenv versions
   pyenv virtualenv 2.7.13 virtual-env-2.7.13
   # 进入某个目录比如/root/work/flask-demo
   pyenv local virtual-env-2.7.13
   # 然后再不需要去手动激活了
   使用 pyenv 来管理多版本的 python 命令，使用 pyenv-virtualenv 插件来管理多版本
   python 包环境。爽歪歪~

# pip
## 包的安装路径
  pip show PACKAGENAME
 一般情况下，包总是被安装在 python 安装目录下的 lib\site-packages\包名\
