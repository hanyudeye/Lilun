---
title: Python办公
permalink: python_office.html
theme: jekyll-theme-cayman
---

这是Python办公的小程序集合

# 批量创建文件

``` bat
for /1 %%i in (0,1,9) do (echo 这是file%%i.txt文件 > file%%i.txt)
```