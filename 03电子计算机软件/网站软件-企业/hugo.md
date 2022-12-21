
## Get Started

<!-- - Step 1: Install Hugo -->

<!-- 下载命令行程序，放在PATH路径下面，Ubuntu 下 直接 apt 安装 -->

- Step 2: Create a New Site
``` shell
hugo new site quickstart
```
- Step 3: Add a Theme 
``` shell
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```
添加配置
``` shell
echo theme = \"ananke\" >> config.toml
``` 

- Step 4: Add Some Content 
```shell
hugo new posts/my-first-post.md
```

- Step 5: Start the Hugo server
```
hugo server -D
```

- Step 6: 部署

```shell
$ cd public
$ git init
$ git remote add origin https://github.com/coderzh/coderzh.github.io.git
$ git add -A
$ git commit -m "first commit"
$ git push -u origin master
```

- Step 7: Build static pages

```shell
hugo -D
```
