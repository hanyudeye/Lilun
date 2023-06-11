
### 往线上mongodb导入数据库
导出打包本地数据库
   
```
mongodump -h 127.0.0.1:27017 -d 数据库名 -o 数据库名
```
打包压缩
  
```
tar zcvf 数据库名-backup.tar.gz 数据库名-backup
```
在服务器创建文件夹
   
```
mkdir dbbackup
```
将压缩包从本地上传到服务器
   
```
scp -P 服务器端口号 ./数据库名-backup.tar.gz 管理员名称@服务器公网IP:/home/管理员名称/dbbackup
```
在服务器上解压缩
  
```
tar xvf 数据库名-backup.tar.gz
```
进入目录`cd 项目名称-backup/`

导入数据库

在服务器更目录下`mongorestore --host 127.0.0.1:29999 -d 数据库名 ./dbbackup/项目名称-backup/数据库名/`

导入成功之后进入数据库`mongo --port 29999`

`use 项目名称` `show tables` `db.项目名称items.find().pretty()`查看表数据

本地导出单表

```
mongoexport -d 数据库名 -c 单表名 -q '{"name": {$ne: null}}' -o ./数据库名-表名.json
```
导入到服务器数据库

```
scp -p 服务器端口号 ./数据库名-表名.json 管理员名称@服务器公网IP:/home/管理员名称/dbbackup
```
在服务器上，进入dbbackup目录

```
mongoimport --host 127.0.0.1:29999 -d 数据库名 -c 表名 ./数据库名-表名.json
```
删除数据库

```
mongo --host 127.0.0.1:29999 -d 数据库名 --eval "db.dropDatabase()"
```

### 为线上数据库配置读取权限
先导入数据库，再配置数据库权限

添加管理员账号，先进入mongodb命令行环境

```
mongo --port 29999
```
切换数据库
   
```
use admin
```
添加管理员

```
db.createUser({user: '管理员名(_owner)', pwd: 'xxx', roles: [{role: 'userAdminAnyDatabase', db: 'admin'}]})
```
对用户登录进行授权，返回1成功
  
```
db.auth('管理员名','密码')   
```
切换到其他数据库
   
```
use 数据库名
```
添加该数据库用户，具备读写操作

```
db.createUser({user: '用户名(数据库名_runner)', pwd: 'xxx', roles: [{role: 'readWrite', db: '数据库名'}]})
```
创建备份角色，备份操作，只能读不能写

```
db.createUser({user: '备份用户名(数据库名_wheel)', pwd: 'xxx', roles: [{role: 'read', db: '数据库名'}]})
```
添加其他数据权限流程，先到admin下授权db.auth，切换到其他数据库，创建用户角色，再创建备份角色

开启验证模式，修改配置文件

```
sudo /etc/mongod.conf
```
将#security:  修改为
 
```
security:
  authorization: 'enabled'
```
重启mongodb
    
```
sudo service mongod restart
```
进入数据库`mongo --port 29999`

直接`show dbs`是没有权限查询

先进入admin`use admin`，再认证`db.auth('管理员名','密码')`

再执行`show dbs`就有权限查询了，`exit`退出数据库

直接登录某个数据库命令 
  
```
mongo 127.0.0.1:29999/数据库名 -u 用户名(数据库名_runner) -p 密码
```
`show tables` `db.logins.find({})`就可以查询数据库了


### 从一台服务器迁移数据到另一个线上mongodb
原理：先从一台服务器将数据库备份到本地，再从本地上传到另一个服务器

在服务器上创建文件夹`mkdir db``cd db`

导出数据库

```
mongodump -h 127.0.0.1:29999 -d 数据库名 -u 备份用户名(数据库名_wheel) -p 密码 -o 输出文件夹(数据库名-old)
```
打包
 
```
tar zcvf 打包文件夹名(数据库名-old.tar.gz) 输出文件夹(数据库名-old)
```
导出单表

```
mongoexport  -h 127.0.0.1:29999 -d 数据库名 -u 备份用户名(数据库名_wheel) -p 密码 -c 单表名 -q '{"name": {$ne: null}}' -o ./输出文件名(数据库名-单表名-old.json)
```
切换到本地命令行，将线上数据库下载到本地

```
scp -P 3389 管理员名@服务器公网IP:/home/管理员名/db/打包文件夹名(数据库名-old.tar.gz) ./
```
将线上单表下载到本地

```
scp -P 3389 管理员名@服务器公网IP:/home/管理员名/db/输出文件名(数据库名-单表名-old.json) ./
```
从本地重新上传数据库到目标服务器

进入目标服务器`mkdir newdb`

上传数据库和单表

```
scp -P 3389 ./输出文件名(数据库名-单表名-old.json) 管理员名@服务器公网IP:/home/管理员名/newdb
scp -P 3389 ./打包文件夹名(数据库名-old.tar.gz) 管理员名@服务器公网IP:/home/管理员名/newdb
```
解压缩tar
   
```
tar xvf 打包文件夹名(数据库名-old.tar.gz)
```
连上数据库`mongo --port 29999 `

`use admin`

`db.auth('管理员名(_owner)','密码')`

创建新数据库

```
use 新数据库名(项目名-数据库名-targt)
db.createUser({user: '项目名-数据库名-targt', pwd: 'xxx', roles: [{role: 'readWrite', db: '新数据库名(项目名-数据库名-targt)'}]})
```
导入数据库

```
mongorestore -h 127.0.0.1:29999 -d 新数据库名 -u 数据库用户名 -p 密码 ./newdb/数据库名-old/数据库名
```
导入单表

```
mongoimport -h 127.0.0.1:29999 -d 新数据库名 -u 数据库用户名 -p 密码 -c users  ./newdb/数据库名-单表名-old.json 
```
检查，登录数据库

```
mongo 127.0.0.1:29999/新数据库名  -u 数据库用户名 -p 密码
```
`show tables``db.users.find({})`

### 数据库备份
在服务器更目录，创建数据库备份执行脚本

```
mkdir tasks
cd tasks
vi 数据库名.backup.sh
```
编辑脚本文件

```
#!/bin/sh

backUpFolder=/home/管理员名/backup/数据库名
date_now=`date +%Y_%m_%d_%H%M`
backFileName=数据库名_$date_now

cd  $backUpFolder
mkdir -p $backFileName

mongodump -h 127.0.0.1:29999 -d 数据库名 -u 数据库名_wheel -p 密码 -o $backFileName

tar zcvf $backFileName.tar.gz $backFileName

rm -rf $backFileName
```
在更目录下，创建文件夹

```
mkdir backup
cd backup
mkdir 数据库名
```
在服务器根目录下执行脚本文件
  
```
sudo sh ./tasks/数据库名.backup.sh
```
启动系统的定时任务 
 
```
crontab -e
```
选择第`2. /bin/nano`

编辑

```
19 00 * * * sh /home/管理员名称/tasks/项目名称.backup.sh
```
//分钟 小时 `control + x` `shift + y`  回车

### 上传数据库备份到七牛私有云
到七牛云官方文档查看nodejs文件上传[https://developer.qiniu.com/kodo/sdk/1289/nodejs#5](https://developer.qiniu.com/kodo/sdk/1289/nodejs#5 "悬停显示")

在tasks目录下创建
 
```
vi upload.js
```

```
var qiniu = require('qiniu');
var config = new qiniu.conf.Config();
// 空间对应的机房
config.zone = qiniu.zone.Zone_z0;
// 是否使用https域名
//config.useHttpsDomain = true;
// 上传是否使用cdn加速
//config.useCdnDomain = true;
var parts = process.env.NODE_ENV.split('@');
var file = parts[1] + '.tar.gz';
var localFile = parts[0] + '/' + file;
console.log(localFile);
var formUploader = new qiniu.form_up.FormUploader(config);
var putExtra = new qiniu.form_up.PutExtra();

var accessKey = '2dAyWqJrZNlHGtWTxdxVsDWlKMvRpDMTh9XqvHod';
var secretKey = 'hAlZcnd_7zv8q9WTDv7bbylNvMC_DDzCEj4hoxta';
var mac = new qiniu.auth.digest.Mac(accessKey, secretKey);
//要上传的空间
bucket = '项目名称deploydb';
var options = {
  scope: bucket,
};
var putPolicy = new qiniu.rs.PutPolicy(options);
var uploadToken=putPolicy.uploadToken(mac);

//上传到奥七牛要保存的文件名
key = file;

// 文件上传
formUploader.putFile(uploadToken, key, localFile, putExtra, function(respErr,
  respBody, respInfo) {
  if (respErr) {
    throw respErr;
  }
  if (respInfo.statusCode == 200) {
    console.log(respBody);
  } else {
    console.log(respInfo.statusCode);
    console.log(respBody);
  }
});
```
再编辑备份脚本文件`vi 项目名称.backup.sh`，在最后一行添加：

```
NODE_ENV=$backUpFolder@$backFileName node /home/管理员名称/tasks/upload.js
```
在tasks目录下，安装七牛模块`cnpm i qiniu`

执行脚本文件`sh ./项目名称.backup.sh`

修改完善定时任务`crontab -e` 每一行命令对应一个任务，可以设置每一天备份一次

安装mysql

```
sudo apt-get install mysql-server mysql-client
```
设置root密码  test123

### 上传项目代码到线上私有git仓库
可选免费的私有git仓库`git.oschina.net`

本地上传私钥到线上仓库，`cd .ssh`，把id_ras.pub内容拷贝到线上git仓库SSH公钥，添加公钥

在本地配置全局的git email和密码

服务器安装git

```
sudo apt-get install git
```
mongoose连接线上数据库方式

```
mongoose.connect('mongodb://username:password@host:port/database?options...');
```
在服务器上创建项目文件夹

```
sudo mkdir /www
cd /www
sudo mkdir 项目名
pwd 项目路径就是/www/项目名
```
赋予管理员修改项目文件夹和production文件夹的读写修改的权限
在www目录下
 
```
sudo chmod 777 项目名
```
进去项目文件夹内
 
```
sudo chmod 777 production
```
在本地项目根目录新建文件`ecosystem.json`

```
{
    "apps": [
        {
            "name": "", //名称
            "script": "server/app.js", //程序入库
            "cwd": "./", //根目录
            "env": {
                "COMMON_VARIABLE": "true"
            },
            "env_production": {
                "NODE_ENV": "production"
            },
            "exec_interpreter": "babel-node",
            "error_file":"./server/logs/app-err.log",//错误输出日志
            "out_file":"./server/logs/app-out.log",  //日志
            "log_date_format":"YYYY-MM-DD HH:mm Z" //日期格式
        }
    ],
    "deploy": {
        "production": {
            "user": "管理员名称",
            "host": [
                "服务器公网IP"
            ],
            "port": "服务器登录端口",
            "ref": "origin/master",
            "repo": "git仓库地址",
            "path": "/www/项目名/production",
            "ssh_options": "StrictHostKeyChecking=no",
            "post-deploy": "cnpm install && npm run build && pm2 startOrRestart ecosystem.json --env production",
            "env"  : {
                "NODE_ENV": "production"
            }
        }
    }
}
```
然后通过git提交代码

在本地项目根目录下，第一次执行拷贝项目代码到服务器上
  
```
pm2 deploy ecosystem.json production setup
```

### 从本地发布上线和更新服务器的nodejs项目
因为pm2在服务器上用的是非交互的ssh连接方式，在服务器更目录下`vi .bashrc`，将这几行注释

```
#case $- in
#    *i*) ;;
#     *) return;;
#esac
```
保存`:wq!` 加载 `.bashrc`      
```
source .bashrc
```

配置nginx反向代理

在服务器根目录下`cd /etc/nginx/conf.d`

编辑配置文件`sudo vi  xxxx-3000.conf`

```
upstream 项目名 {
  server 127.0.0.1:3000;
}

server {
  listen 80;
  server_name 域名地址(xxx.xxx.com);

  location / {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-Nginx-Proxy true;
    proxy_pass http://项目名;
    proxy_redirect off;

  }
  
  location ~* ^.+\.(jpg|jpeg|gif|png|ico|css|js|pdf|txt) {
    root /www/项目名称/production/current/client/dist;
  }
}
```
保存，重启服务器
 
```
sudo nginx -s reload
```
如果有防火墙需打开防火墙相应端口

```
sudo /etc/iptables.rules
```
增加两行
 
```
-A INPUT -s 127.0.0.1 -p tcp --destination-port 3000 -m state --state NEW,ESTABLISHED -j ACCEPT
-A OUTPUT -d 127.0.0.1 -p tcp --source-port 3000 -m state --state ESTABLISHED -j ACCEPT
```
保存，重启防火墙
  
```
sudo iptables-restore < /etc/iptables.rules
```

本地修改同步到线上服务器

首先保证本地代码修改后提交git

将代码同步到线上，并启动服务,在本地项目执行命令

```
pm2 deploy ecosystem.json production
```
线上服务器需要全局安装`babel-cli`


### 项目部署的一般流程总结
1.在dnspod域名管理网站添加二级子域名

2.在本地项目后端服务入口文件写好没有用过的端口号

3.本地项目，修改mongodb本地和线上的连接方式，线上写好用户名和密码

4.本地，写好发布脚本ecosystem.json，修改名字，仓库地址，服务器ip，端口号

5.服务器上，在/www下新建项目文件夹，授权文件夹`sudo chomd 777 文件夹名`

6.服务器下，新增nginx配置文件，在`/etc/nginx/conf.d`, 可直接复制其他配置文件`sudo cp 文件夹名 文件夹名` ，编辑nginx 配置文件，`sudo vi ...` 修改域名，端口号，名称

7.在本地，先提交代码到仓库

8.部署代码，第一次，初始化服务器项目目录结构，`pm2 deploy ecosystem.json production setup`，第二次部署发布`pm2 deploy ecosystem.json production`

9.在服务器上，检查`pm2 list` ,如有问题，不断重启，先停pm2服务，检查日志，`pm2 logs`

10.修改防火墙，`sudo vi /etc/iptables.rules`，增加新的端口，

   重启防火墙，`iptables-restore < /etc/iptables.rules`
   
   重启`nginx  sudo nginx -s reload`

### 申请选购SSL证书
国内，又拍云 ，腾讯云，阿里云，七牛云，推荐腾讯云

管理中心-》云产品-》ssl证书管理-》申请证书->手动DNS验证》查看证书详情

复制主机记录，记录值-》dnspod-》添加记录，cname方式粘贴主机记录和记录值，再添加对应A记录  域名和服务器ip

腾讯云查询-》下载证书

在本地下载的证书nginx目录下上传到服务器更目录
   
```
scp -P 3389 ./2_mini.iblack7.com.key 管理员名@....:/home/管理员名/
scp -P 3389 ./1_mini.iblack7.com.bundle.crt 管理员名@....:/home/管理员名/
```
再上传free的证书 ，再执行一遍上面的代码

在服务器根目录

```
mkdir ssl
mv 1_*  ./ssl/
mv 2_*  ./ssl/
sudo mv ssl /www/
```

证书安装可参考 腾讯云 证书管理，详情，执行文档，nginx安装方法，复制server,不要复制location部分

修改nginx配置文件，在服务器上进入 `cd /etc/nginx/conf.d`

修改文件夹名，带上free开头， `sudo vi free。。`

粘贴代码到server部分

`listen 443`  ssl证书访问的端口号

`server name` 证书绑定的域名

`ssl on` 启动ssl认证

`ssl_certificate /www/ssl/1_free.._bundle.crt`

`ssl_certificate_key /www/ssl/2_free..key`

`ssl_protocols`   ssl证书所配置的协议

`ssl_ciphers`   加密套件

location部分不用改，具体代码如下：

```
upstream free {
}

再加一个server部分
server {
  listen 80 
  server_name app....com
  #rewrite ^(.*)  https://$host$1 permanent;
  return  301 https://app.xxx.com$request_url; 
}

server {
  listen 443;
  server_name free.xxx.com
  ...

  proxy_pass http://free
  最底下加一行
  if($ssl_protocols = "") {
    rewrite ^(.*)  https://$host$1 permanent;
  }
}
```
修改另外一个nginx配置文件

检查配置文件有没有错误`sudo nginx -t` 检查配置文件有没有错误

重启nginx服务`sudo nginx -s reload`