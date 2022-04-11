/*
 * @Descripttion: 
 * @version: 
 * @Author: hanyudeye
 * @Date: 2022-04-05 14:56:16
 * @LastEditTime: 2022-04-05 14:58:53
 */

const http=require('http');

const hostname='127.0.0.1';
const port=3000;

const server=http.createServer((req,res)=>{

    res.statusCode=200;
    res.setHeader('Content-Type','text/plain');
    res.end('Hello,world!\n');
});

server.listen(port,hostname,()=>{

    console.log(`server running at http://${hostname}:${port}/`);
});