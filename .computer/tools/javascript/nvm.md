---
title: nvm使用教程
permalink: .html
theme: jekyll-theme-cayman
---

## nvm 命令  (node.js 版本管理工具)

用浏览器打开：  https://github.com/coreybutler/nvm-windows/releases

- nvm arch  显示CPU体系
- nvm install <version> [arch]  安装某个版本的 node.js
- nvm list [available] 列出已安装的 node.js
- nvm use <version>  使用某个版本的 node.js
- nvm on  允许 nvm 管理 node.js
- nvm off 禁止 nvm 管理 node.js

添加国内镜像配置: 

settings.txt 文件中添加：

node_mirror: https://npm.taobao.org/mirrors/node/
npm_mirror: https://npm.taobao.org/mirrors/npm/

## Webpack 项目打包工具 module

随着 SPA（Single Page App) 单页应用的发展，大家发现，使用的js/css/png等文件特别多。难以管理。文件夹结构很容易混乱。

```
$ npm install --save-dev webpack
```
## 安装 vuejs  (这里是vue 2 的构建过程，有点过时了)


要同时安装 `vue`和 `vue-cli`这两个node package.

运行下面这个命令：

```
$ npm install vue vue-cli -g
```

`-g` 表示这个包安装后可以被全局使用。 


创建一个基于 webpack 模板的新项目:

```
$ vue init webpack my-project
```

注意： 我们使用Vue, 都是在 `webpack` 这个大前提下使用的。

安装依赖:

```
$ cd my-project
$ cnpm install
```

在本地，以默认端口来运行：

```
$ npm run dev
```



## 
