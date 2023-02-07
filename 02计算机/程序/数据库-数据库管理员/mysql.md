> 关系型数据库：设置关系结构用来存储数据
> sql: 查询结构化数据的语法


## 数据堆
![](images/2022-11-12-05-38-46.png)

## 怎么在数据堆中处理数据

用到了 操作数据的语法 . (增删改查)

## 配置文件 /etc/mysql/my.cnf

``` cnf
max_connections = 10
log-slow-queries
long_query_time = 5
```

## 连接数据库

```
mysql> mysql -h192.168.206.100 -uroot -p12345678; /*u与root可以不加空格*/
```

