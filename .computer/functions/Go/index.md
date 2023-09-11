---
title: Go语言编码
permalink: .html
theme: jekyll-theme-cayman
---

# 1. 设置代理

如果网络不畅通，需要设置代理

1. go env -w GOPROXY=https://代理地址
go env -w GOPROXY=http://goproxy.io,direct,timeout=5s

在此示例中，我们指定http://Goproxy.io为主要代理服务器，并使用“direct”作为备用服务器（如果http://Goproxy.io无法访问）,超时设置为5秒

