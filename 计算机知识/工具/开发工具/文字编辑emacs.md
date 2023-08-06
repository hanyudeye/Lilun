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


## 在ubuntu 中使用emacs
2022年了搜了一堆网站，最终发现解决这个问题有好几个细节很多热门的答案都没有讲清楚，我的系统是Debian, 首先你要确定你有zh_CN.utf8这个locale,那些答案的设定才有意义

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
内部内容如下

#!/bin/bash
LC_CTYPE="zh_CN.utf8" emacs
然后修改 /usr/share/applications/emacs.desktop 中的 TryExec 和 Exec 为

TryExec=/usr/bin/my_emacs
Exec=/usr/bin/my_emacs
这样点击图标启动就也能支持中文了。 更多 .desktop 文件的细节，google linux freedesktop desktop file entry key


## 如何在spacemacs中快速导航项目

在Spacemacs中，你可以使用一些快捷键和功能来快速导航项目。以下是一些常用的方法：

1. **使用Projectile插件**：Spacemacs内置了Projectile插件，它可以帮助你管理和导航项目。你可以使用`SPC p`作为前缀键来执行一系列与项目相关的操作。例如，`SPC p f`可以用于查找文件，`SPC p p`可以切换到不同的项目，`SPC p b`可以列出项目中的缓冲区等。

2. **使用文件导航器**：Spacemacs支持多个文件导航器，如NeoTree和Treemacs。你可以使用`SPC f t`来打开NeoTree，或者使用`SPC f T`来打开Treemacs。这些导航器可以显示项目的目录结构，让你快速浏览和打开文件。

3. **使用搜索功能**：Spacemacs内置了强大的搜索功能。你可以使用`SPC s p`来搜索项目中的文件，使用`SPC s P`来搜索项目中的内容。这些搜索功能可以帮助你快速找到你需要的文件或代码片段。

4. **使用跳转命令**：Spacemacs提供了一些跳转命令，可以让你在项目中快速导航。例如，你可以使用`SPC j j`来跳转到一个特定的文件，使用`SPC j l`来跳转到一个特定的行，使用`SPC j s`来跳转到一个特定的符号等。

5. **使用快速打开功能**：Spacemacs有一个快速打开功能，可以让你快速打开最近浏览过的文件。你可以使用`SPC f f`来打开最近的文件，使用`SPC f r`来打开最近的项目。

这些方法可以帮助你在Spacemacs中快速导航项目。根据你的个人偏好和项目需求，选择适合你的方式来提高效率。

