---
layout: default
toc: false
title: 使用 MySql 进行 数据整理
date:  2023-09-01T09:47:31+08:00
categories: ['sql']
---


MySql 其实就是一组快递柜，要整理的数据一个个放在快递柜里面，节约空间，也方便查找。

> 通过柜子的序列编号查找
 

# 工具的使用

``` sql
/* 连接数据库，打开 网络资源  柜子 */
mysql> mysql -h192.168.206.100 -uroot -p12345678; /*u与root可以不加空格*/
```

``` sql
use mysql;
/* 设置密码，在新版本过时了，不存在 password 字段了 */
SET PASSWORD FOR'root'@'127.0.0.1'=PASSWORD('password');
/* 更新密码 */
update user set password=password("123") where user="root";
```

``` sql
/* 授权 */
GRANT ALL ON db1.*TO'kerry'@'localhost'IDENTIFIED BY'beck123';

/* 更新数据库信息 */
FLUSH PRIVILEGES
```
# 数据库操作

```sql

/* 创建数据库 */
create database bookstore;
use bookstore;

create table books(
book_id int,
title varchar(50),
author varchar(50)
);

insert into books (book_id,title,author) values (1,"gogo","lily");

delete from books where book_id=1;

describe books;

alter Table books
change Column book_id book_id int auto_increment primary key,
change column author author author_id int,
add column description text,
add column genre ENUM ('novel','poetry','drama');

/* 修改数据 */
update books set author="xli" where book_id=13;

```


