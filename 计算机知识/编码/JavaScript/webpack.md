---
title: webpack
permalink: webpack.html
theme: jekyll-theme-cayman
---

Webpack 是一个web文件打包工具，提高程序的执行效率（加载与运行）

1. 安装Webpack

首先，你需要安装Webpack。你可以使用npm（Node.js包管理器）来安装Webpack。在命令行中运行以下命令：

```
npm install webpack webpack-cli --save-dev
```

这将安装Webpack和Webpack命令行工具。

2. 创建Webpack配置文件

在项目根目录下创建一个名为webpack.config.js的文件。这个文件是Webpack的配置文件，它告诉Webpack如何打包你的应用程序。

以下是一个简单的Webpack配置文件示例：

```
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

这个配置文件告诉Webpack将src目录下的index.js文件作为应用程序的入口点，并将打包后的文件输出到dist目录下的bundle.js文件中。

- 查找入口文件index ，打包到 dist下的bundle 文件 

3. 创建JavaScript文件

在src目录下创建一个名为index.js的JavaScript文件。这个文件将作为你的应用程序的入口点。

以下是一个简单的JavaScript文件示例：

```
function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet('World');
```

这个JavaScript文件定义了一个greet函数，它将一个名字作为参数，并在控制台中打印出一条问候语。

4. 打包JavaScript文件

现在，你可以使用Webpack来打包你的JavaScript文件了。在命令行中运行以下命令：

```
npx webpack
```

这将使用Webpack默认配置文件（webpack.config.js）来打包你的JavaScript文件。

5. 运行应用程序

现在，你已经成功地将JavaScript文件打包成一个文件。你可以在浏览器中打开dist目录下的bundle.js文件，或者在HTML文件中引用它，以运行你的应用程序。

以上是一个简单的Webpack教程，帮助你了解如何使用Webpack构建JavaScript应用程序。当然，Webpack还有很多高级功能，如代码拆分、代码优化等，你可以在Webpack官方文档中了解更多。

## webpack

- 初始化 npm init -y
- 下载依赖  npm  i webpack webpack-cli -D
- 编译 (开发模式)  npx webpack  ./src/main.js --mode=development
- 生产模式 npx webpack ./src/main.js --mode=production

## 配置webpack.config.js
采用 Common.js 模块化规范

``` js
module.exports = {
  // 入口
  entry: "",
  // 输出
  output: {},
  // 加载器
  module: {
    rules: [],
  },
  // 插件
  plugins: [],
  // 模式
  mode: "",
};
```

- 开发模式：development
- 生产模式：production


``` js
// Node.js的核心模块，专门用来处理文件路径
const path = require("path");

module.exports = {
  // 入口
  // 相对路径和绝对路径都行
  entry: "./src/main.js",
  // 输出
  output: {
    // path: 文件输出目录，必须是绝对路径
    // path.resolve()方法返回一个绝对路径
    // __dirname 当前文件的文件夹绝对路径
    path: path.resolve(__dirname, "dist"),
    // filename: 输出文件名
    filename: "main.js",
  },
  // 加载器
  module: {
    rules: [],
  },
  // 插件
  plugins: [],
  // 模式
  mode: "development", // 开发模式
};
```

## 处理样式资源

### 处理 Css 资源

1. 下载包

``` sh
npm i css-loader style-loader -D
```
2. 功能介绍

- css-loader：负责将 Css 文件编译成 Webpack 能识别的模块
- style-loader：会动态创建一个 Style 标签，里面放置 Webpack 中 Css 模块内容

此时样式就会以 Style 标签的形式在页面上生效

3.  配置
``` js
const path = require("path");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "main.js",
  },
  module: {
    rules: [
      {
        // 用来匹配 .css 结尾的文件
        test: /\.css$/,
        // use 数组里面 Loader 执行顺序是从右到左
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  plugins: [],
  mode: "development",
};
```

添加 Css 资源

``` js
import count from "./js/count";
import sum from "./js/sum";
// 引入 Css 资源，Webpack才会对其打包
import "./css/index.css";

console.log(count(2, 1));
console.log(sum(1, 2, 3, 4));

```
