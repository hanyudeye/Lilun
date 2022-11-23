
## 中级 Python

是一本python 相关的小书


### 趁手的工具

- 搭建一个场景（环境）
- 调试
- 反馈


#### 虚拟环境
![](images/2022-11-23-10-39-48.png)
因为有 两个 差异的 python ，所以要分开处理
所以系统中 最好有 两个 不同的 python , 这是要给 Python 一个 各自的环境


可以使用 ```virtualenv``` 工具

安装
``` sh
$ pip install virtualenv
```

使用

```sh
$ virtualenv myproject
$ source myproject/bin/activate
```

如果你想让你的 virtualenv 使用系统全局模块，请使用 ```--system-site-packages``` 参数创建你的 virtualenv，例如：

```sh
virtualenv --system-site-packages mycoolproject
```

使用以下命令可以退出这个 virtualenv:

```sh
$ deactivate
```

运行之后将恢复使用你系统全局的 Python 模块。


## 调试（Debugging）

利用好调试，能大大提高你捕捉代码Bug的能力。大部分新人忽略了 Python debugger（```pdb```） 的重要性。在这个章节我只会告诉你一些重要的命令，你可以从官方文档中学习到更多。

> 译者注，参考：https://docs.python.org/2/library/pdb.html
或者 https://docs.python.org/3/library/pdb.html

### 从命令行运行

你可以在命令行使用Python debugger运行一个脚本，举个例子：

```bash
$ python -m pdb my_script.py
```

这会触发 debugger 在脚本第一行指令处停止执行。这在脚本很短时会很有帮助。你可以通过（Pdb）模式接着查看变量信息，并且逐行调试。

### 从脚本内部运行

同时，你也可以在脚本内部设置断点，这样就可以在某些特定点查看变量信息和各种执行时信息了。这里将使用 ```pdb.set_trace()``` 方法来实现。举个例子：

```python
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())
```

试下保存上面的脚本后运行之。你会在运行时马上进入 debugger 模式。现在是时候了解下 debugger 模式下的一些命令了。

##### 命令列表：

- ```c```: 继续执行
- ```w```: 显示当前正在执行的代码行的上下文信息
- ```a```: 打印当前函数的参数列表
- ```s```: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
- ```n```: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）

单步跳过（```n```ext）和单步进入（```s```tep）的区别在于，单步进入会进入当前行调用的函数内部并停在里面，而单步跳过会（几乎）全速执行完当前行调用的函数，并停在当前函数的下一行。

## 类

``` python

```