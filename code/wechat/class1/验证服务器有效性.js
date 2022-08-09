/*
 * @Author: hanyudeye@163.com
 * @Date: 2022-04-04 14:03:58
 * @Description: 
 */

//引入 express 模块
const express = require('express');

// 创建 app应用对象 
const app=express();
//验证服务器的有效性

app.use((req,res,next)=>{


})

//监听端口号
app.listen(3000,()=>console.log("服务器启动成功"));