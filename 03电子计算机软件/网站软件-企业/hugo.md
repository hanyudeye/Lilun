Hugo 可以根据 模板 生成 **静态网站**，

## 使用

- 创建hugo 网站

``` shell
hugo new site quickstart
```
- 添加主题

``` shell
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```

- 添加配置
``` shell
echo theme = \"ananke\" >> config.toml
``` 
$ git clone https://github.com/olOwOlo/hugo-theme-even themes/even

- 添加文章

```shell
hugo new posts/my-first-post.md
```

- 开启服务
``` sh
hugo server 
```

- 部署

```shell
$ cd public
$ git init
$ git remote add origin https://github.com/coderzh/coderzh.github.io.git
$ git add -A
$ git commit -m "first commit"
$ git push -u origin master
```
- 构建静态页面
``` sh
hugo server -D
```
