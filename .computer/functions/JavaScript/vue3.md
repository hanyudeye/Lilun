---
layout: default
toc: false
title: vue3使用教程
date:  2023-08-29T10:15:15+08:00
categories: ['vue3']
---



Vue 关注 MVC 模式中的视图，做的是 视图的渲染，视图组件化

教程： https://24kcs.github.io


## 创建Vue3项目

- npm init vue@latest  -g  全局安装
- vue create project 安装project项目
- cd project 进入project项目
- npm run server 运行 , 访问地址 http://localhost:8080/
- npm run build  构建


## vue3 基本功能

- 视图组件

```js
    Vue.component('button-counter',{
    data:function(){
    return{
        count:0
    }
    },
        template:'<button v-on:click="count++">我被点击了{{count}}次!</button>' 
    })
```

- 数据绑定

对于需要经常刷新的UI元素，与数据建立绑定非常实用，就可以使用到数据的处理方式，如计算，函数，事件。

- 单文件组件
为适应复杂项目，Vue支持以.vue为扩展名的文件定义一个完整的组件，用以替代使用 Vue.component注册组件的形式。开发者可以使用 Vite或 Webpack 等构建工具打包单文件组件。

- Vue Router: 允许开发者编写在多个视图中切换的单网页应用程序
- Vue Server Render: Vue.js 的服务器端渲染(SSR)

