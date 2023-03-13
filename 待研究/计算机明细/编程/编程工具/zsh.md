## 插件

### 代理

```sh
# 启动代理
proxy () {
  export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7891
  echo "HTTP Proxy on"
}

# 关闭代理
noproxy () {
  unset http_proxy
  unset https_proxy
  unset all_proxy
  echo "HTTP Proxy off"
}
```