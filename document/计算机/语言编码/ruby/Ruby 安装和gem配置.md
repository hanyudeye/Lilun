---
title: rvm ，rbenv, gemset 的使用
permalink: ruby.html
theme: jekyll-theme-cayman
--- 

# 使用 rvm 对 Ruby 进行版本控制
安装
``` shell
$ curl -L get.rvm.io | bash -s stable
``` 

1. 列出ruby的版本
``` shell
$ rvm list
```
2. 安装 ruby
``` shell
$ rvm install ruby-3.0.0
```

3. 使用特定版本的 ruby

``` shell
$ rvm use 版本号
```

4. 卸载

``` shell
$ rvm remove 版本号
```

# rbenv 另一个 ruby 版本管理

``` shell
#安装
$ rbenv install 3.0.1
# 使用某个版本
$ rbenv global 3.0.1
# 显示目前版本 
$ ruby -v
``` 

# gemset 的使用

gem 是 ruby 的 包管理器

### 配置国内镜像

``` shell
$ gem sources --remove https://rubygems.org/
$ gem sources -a http://ruby.taobao.org/
$ gem sources -l
*** CURRENT SOURCES ***

http://ruby.taobao.org
# 请确保只有 ruby.taobao.org
``` 

### 安装包 
``` shell
$ gem install  包名
``` 

### 问题
1. 没有权限

如果出现
``` 
 You don't have write permissions for the /var/lib/gems/2.7.0
``` 

可以把目录设置在 用户目录
``` shell
$ echo 'export GEM_HOME=~/.ruby/' >> ~/.bashrc
$ source ~/.bashrc
``` 
