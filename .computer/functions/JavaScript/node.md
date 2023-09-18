
# Node.js 默认提供 npm 包管理器，Corepack 为您提供 Yarn 和 pnpm，而无需安装它们。

corepack enable

# npx

npx是npm5.2.0及以上版本中提供的一个命令行工具，它可以帮助你在不全局安装包的情况下执行包中的命令。下面是一个简单的npx教程，帮助你了解如何使用npx。

1. 执行本地安装的包

你可以使用npx来执行本地安装的包中的命令。例如，如果你已经在项目中安装了webpack包，你可以使用以下命令来执行webpack命令：

```
npx webpack
```

这将在项目中查找webpack包，并执行它的命令。

2. 执行远程包中的命令

你也可以使用npx来执行远程包中的命令。例如，如果你想要使用create-react-app包来创建一个新的React应用程序，你可以使用以下命令：

```
npx create-react-app my-app
```

这将在你的计算机上下载create-react-app包，并使用它来创建一个名为my-app的新React应用程序。

3. 执行不同版本的包中的命令

如果你需要在不同的包版本之间切换，你可以使用npx来执行不同版本的包中的命令。例如，如果你需要使用不同版本的webpack包来构建你的应用程序，你可以使用以下命令：

```
npx webpack@4.44.2
```

这将在你的计算机上下载webpack@4.44.2包，并使用它来构建你的应用程序。

4. 执行GitHub上的命令

如果你需要执行GitHub上的命令，你可以使用npx来执行它们。例如，如果你想要使用GitHub上的http-server包来启动一个本地服务器，你可以使用以下命令：

```
npx http-server
```

这将在你的计算机上下载http-server包，并使用它来启动一个本地服务器。

以上是一个简单的npx教程，帮助你了解如何使用npx。npx的功能非常强大，你可以在官方文档中了解更多。

# nvm
> 软件安装器

NVM, 全名为"Node Version Manager", 是非常好用的Node版本管理器。 

升级到到定制版
$ nvm install 13.10.0

升级到最新版
$ nvm install lastest

升级到稳定版
$ nvm install stable

- nvm list available (windows) 列出所有安装的版本
- nvm list-remote (linux/mac)
- nvm list  列出本地安装好了的版本
- nvm install 10.5.1 安装某个版本
- nvm use 10.5.1 当前文件夹指定node 的版本
- nvm alias default 10.5.1 系统全局使用某个版本


npm config delete prefix
npm config set prefix $NVM_DIR/versions/node/v19.5.0


