# NVM， NPM 与 Node

NVM, 全名为"Node Version Manager", 是非常好用的Node版本管理器。 

- 安装地址

Linux/Mac下的NVM官网：https://github.com/creationix/nvm 
Windows下的NVM官网： https://github.com/coreybutler/nvm-windows


- 设置环境变量：
```
NVM_HOME 		D:\nvm
NVM_SYMLINK     C:\Program Files\nodejs
```

## 命令

- nvm list available (windows) 列出所有安装的版本
- nvm list-remote (linux/mac)
- nvm list  列出本地安装好了的版本
- nvm use 10.5.1 当前文件夹指定node 的版本
- nvm alias default 10.5.1 系统全局使用某个版本


## 修改镜像服务器

- NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/dist nvm install

对于NPM (安装某些npm第三方包时使用), 则用cnpm代替 npm 命令。 

```
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```

对于Linux, Mac用户，可以通过直接创建一个 "alias" 命令： 

```
alias cnpm="npm --registry=https://registry.npm.taobao.org \
--cache=$HOME/.npm/.cache/cnpm \
--disturl=https://npm.taobao.org/dist \
--userconfig=$HOME/.cnpmrc"
```

然后，就可以通过国内的淘宝服务器来安装node的包了，例如：

```
$ cnpm install vue-cli -g
```
