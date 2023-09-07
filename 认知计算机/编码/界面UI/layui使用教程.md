---
layout: default
toc: false
title: layui使用教程
date:  2023-09-01T10:22:44+08:00
categories: ['ui']
---

Layui 是一套开源的 Web UI 组件库，采用自身轻量级模块化规范，遵循原生态的 HTML/CSS/JavaScript 开发模式，极易上手，拿来即用。其风格简约轻盈，而内在雅致丰盈，甚至包括文档在内的每一处细节都经过精心雕琢，非常适合网页界面的快速构建。Layui 区别于一众主流的前端框架，却并非逆道而行，而是信奉返璞归真之道。确切地说，它更多是面向于追求简单的务实主义者，即无需涉足各类构建工具，只需面向浏览器本身，便可将页面所需呈现的元素与交互信手拈来。

<!--more-->

## 安装

- npm i layui
- 引入

``` html
<!-- 引入 layui.css -->
<link href="//unpkg.com/layui@2.8.0/dist/css/layui.css" rel="stylesheet">
 
<!-- 引入 layui.js -->
<script src="//unpkg.com/layui@2.8.0/dist/layui.js">
```

## 快速上手

``` html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Quick Start - Layui</title>
  <link href="/cdn.staticfile.org/layui/2.8.0/css/layui.css" rel="stylesheet">
</head>
<body>
  <!-- HTML Content -->
  <script src="/cdn.staticfile.org/layui/2.8.0/layui.js"></script>
  <script>
  // Usage
  layui.use(function(){
    var layer = layui.layer;
    // Welcome
    layer.msg('Hello World', {icon: 6});
  });
  </script> 
</body>
</html>
```

##  栅格布局 (合理定位对象位置)

> 格子布局，就像格子存放数据一样，可以使数据（对象）摆放整齐。

- .col-xs- (手机)	.col-sm- (平板)	.col-md-(台式)	.col-lg- (电视)

- 始终等比例水平排列：
- layui-row
- layui-col-xs6  

- 移动设备、桌面端的组合响应式展现：
- layui-col-xs12 layui-col-md8

- 移动设备、平板、桌面端的复杂组合响应式展现：
- layui-col-xs6 layui-col-sm6 layui-col-md4

- 列间隔：
- layui-col-space1
- layui-col-space32

即：支持列之间为 1px-32px 区间的所有双数间隔，以及 1px、5px、15px、25px 的单数间隔
 
事实上 `IE8/IE9` 并不支持 `Media Queries`，但你可以使用下面的补丁进行兼容（补丁来自于开源社区）：

```
<!-- 让 IE8/9 支持媒体查询，从而兼容栅格 -->
<!--[if lt IE 9]>
  <script src="https://cdn.staticfile.org/html5shiv/r29/html5.min.js"></script>
  <script src="https://cdn.staticfile.org/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->
```

## 导航菜单

一般用于页面头部菜单。样式规则如下：

- 通过 `class="layui-nav"` 设置导航容器
- 通过 `class="layui-nav-item"` 设置导航菜单项
  - 追加 `className` 为 `layui-this` 可设置菜单选中项
- 通过 `class="layui-nav-child"` 设置导航子菜单项
  - 追加 `className` 为 `layui-nav-child-c` 和 `layui-nav-child-r` 可设置子菜单居中和向右对齐
- 给导航容器追加任意背景色 layui-bg-gray ,blue ,green

垂直导航
一般用于左侧侧边菜单。样式规则如下：

- 在水平导航的 `class` 规则上，通过设置 `class="layui-nav layui-nav-tree"` 定义垂直导航容器。
- 通过 `class="layui-nav-itemed"` 设置父菜单项为展开状态
- 通过给导航容器追加 `class="layui-nav-side"` 可设置侧边垂直导航
- 其余结构及填充内容与水平导航完全相同

