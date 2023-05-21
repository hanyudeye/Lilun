
### node更新到最新版

``` sh
# 升级到到定制版
$ nvm install 13.10.0

# 升级到最新版
$ nvm install lastest

# 升级到稳定版
$ nvm install stable
```

### 使用 nvm
```
npm config delete prefix
npm config set prefix $NVM_DIR/versions/node/v19.5.0
```

### 使用npm命令时报错误Error: EACCES: permission denied，如何解决 

改变npm默认的路径。
步骤如下：
进入终端，依次输入一下命令
（1）创建global安装任务的目录
mkdir ~/.npm-global
（2）配置npm使用新的目录
sudo npm config set prefix '~/.npm-global'
（3）在~/.profile文件中增加配置
sudo export PATH=~/.npm-global/bin:$PATH
（4）配置文件立即生效
source ~/.profile
（5）重新执行命令
sudo npm install -g xxxx 


## webpack

- 初始化  npm init -y 
- 下载 webpack   npm i webpack webpack-cli -D
- 
