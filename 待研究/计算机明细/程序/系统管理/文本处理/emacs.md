## emacs [大]编辑器

编辑器： 是 书写 文字的 工具，重点用到来输入终端 **键盘** ,而在手机上，可能会用到手写笔或者语音翻译。

emacs 书写文字的时候，提供了很多处理文字的命令，还可以自己扩展，所以很强大


## 配置 .emacs 启动文件 或 其它

### 配置快捷键

```lisp
(define-key keymap "keystroke" 'command-name)
(global-set-key "keystroke" 'command-name)
(local-set-key "keystroke" 'command-name) 
(global-set-key "\C-xl" 'goto-line)
```
### 抑制默认的初始化

``` lisp
(setq inhibit-default-init t) ; no global initialization
```


## 扩展

### treemacs
文件目录

### eww

| Key binding   | Description      | Function         |
|---------------+------------------+------------------|
| ~SPC a w e e~ | Start eww        | eww              |
| ~SPC a w e w~ | List eww buffers | eww-list-buffers |

### 任务管理 agenda
