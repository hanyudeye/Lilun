---
title: Vue.js 权威指南
--- 

Vue.js 不是一个框架，而是一个视图。此视图与数据进行绑定。

## 数据绑定

语法 :  {{var}}

数据绑定的同时，还能进行表达式运算与函数运算

对标签，也能执行指令，这是间接可以操作 html 元素

## 指令

### 注册自定义指令

#### Vue.directive

## 计算属性
模板中的表达式存在过多逻辑，可以使用计算属性

``` js

        computed: {
            didiFamily: {
                // 一个计算属性的getter
                get: function() {
                    // 'this' 指向 vm 实例
                    return this.didi + this.family
                },
                // 一个计算属性的setter
                set: function(newVal) {
                    var names = newVal.split('')
                    this.didi = name[0]
                    this.family = names[1]
                }
            },
} 
```
## 组件 components

### Templates

## Components building blocks
### Directives
### Events
### Methods
### Watchers
### Computed Properties
### Methods vs Watchers vs Computed Properties
### Props
### Slots
### Filters
