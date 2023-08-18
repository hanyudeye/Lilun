---
title: 文字编辑 emacs
permalink: .html
theme: jekyll-theme-cayman
---

- 编写或修改文字
- 编写或修改代码
- 用户可扩展的编辑器 emacs

# emacs

## Command Line and Script

Start emacs ignoring the file:~/.emacs.d/init.el or file:~/.emacs configuration file.

``` sh
$ emacs --no-init-file

or 

$ emacs -q
```

Start Emacs with a custom configuration file

``` shell
$ emacs -q -l custom.el

```

Debug Emacs configuration file: ~/.emacs.d/init.el or ~/.emacs

```shell
$ emacs  --debug-init
```


## Configuration

### Turn-off Cursor Blink

``` elisp
(blink-cursor-mode -1)
```
### Turn-off Startup Screen

``` elisp
(setq inhibit-startup-screen t)
```
### Set Default Web Browser

Set the default web browsr used by (browse-url <url>) function and by org-mode.

``` elisp
(setq browse-url-browser-function 'browse-url-generic
      browse-url-generic-program "chromium-browser")

```
### Hide / Show Emacs Widgets

#### Hide / Show Menu bar

Hide Menu Bar  
> (menu-bar-mode 0)


#### Hide / Show Scroll Bar

Show  
> (scroll-bar-mode 1)

### Separte Customization from init file 

It will keep the user customization created with M-x customize-theme,
M-x customize-group in a separate file ~/.emacs.d/custom.el.

```elisp
(setq custom-file (concat (file-name-as-directory user-emacs-directory)
                            "custom.el"
                            ))
(load custom-file 'noerror)
```


## 在ubuntu 环境中，emacs 使用中文

系统是Debian, 首先确定你有zh_CN.utf8这个locale

locale -a | grep -i zh_CN
如果没有，下面的命令安装

sudo apt install -y locales
dpkg-reconfigure locales 

弹出的图形界面直接选 all, 装完之后用之前的命令验证一下能找到 zh_CN.utf8 了 下面的命令行启动支持中文

LC_CTYPE="zh_CN.utf8" emacs
为了避免麻烦，每次都要写这堆前缀，可以改 ~/.bashrc 最后面加上

export LC_CTYPE="zh_CN.utf8"
改完重新加载一次生效

source ~/.bashrc
这个时候验证一下直接输入 emacs 命令启动，也能输入中文了

对于桌面图标，需要改一下 /usr/share/applications/emacs.desktop 文件

本来呢，直接把其中的 TryExec 和 Exec 前面都加上上面的那段 LC_CTYPE="zh_CN.utf8" 代码前缀就行了,但是因为 desktop 文件本身会识别等号，所以这段代码含等号就不能这样加了，先在/usr/bin 创建个新的命令

sudo touch /usr/bin/my_emacs
sudo chmod +rwx my_emacs

#!/bin/bash
LC_CTYPE="zh_CN.utf8" emacs
然后修改 /usr/share/applications/emacs.desktop 中的 TryExec 和 Exec 为

TryExec=/usr/bin/my_emacs
Exec=/usr/bin/my_emacs
这样点击图标启动就也能支持中文了。 更多 .desktop 文件的细节，google linux freedesktop desktop file entry key


