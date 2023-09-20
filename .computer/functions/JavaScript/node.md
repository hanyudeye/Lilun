
# Node.js 默认提供 npm 包管理器，Corepack 为您提供 Yarn 和 pnpm，而无需安装它们。

corepack enable

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


