---
title: vue.js2 学习手册
---


文档 https://cn.vuejs.org/v2/guide/

## Vuejs 环境的搭建
### 使用 script 标签

```html
<!-- 开发环境版本，包含了有帮助的命令行警告 -->
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<!-- 生产环境版本，优化了尺寸和速度 -->
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

### 使用 vue-cli 脚手架

```sh
npm install -g @vuel/cli
vue create my-app
cd my-app
npm run serve
```

常见的插件
- Webpack：代码模块化构建打包工具。
- Gulp：基于流的自动化构建工具。
- Babel：使用最新的 规范来编写 js。
- Vue：构建数据驱动的Web界面的渐进式框架
- Express：基于 Node.js 平台，快速、开放、极简的 Web 开发框架。



## jQuery 与 Vue 区别
jQuery
``` js
if(showBtn){
var btn=$('<button>Click me</button>');
btn.on('click',function(){});

$('#app').append(btn);

}

```

Vue
```
<div id="app">
<button v-if="showBtn" v-on:click="handleClick">Click me</button>
</div>

<script>
new Vue({
el:'#app',
data:{
showBtn:true
}
});

</script>

```

### 内部指令

v-if           条件为 false 的 Dom 对象会被删除
v-show    条件为 false 的 Dom 对象会被隐藏
v-model   与 input ,select ,text,checkbox ,radio 等表单元素建立双向绑定   (可选参数 number ,lazy,debounce )
v-for        重复渲染
v-text       等效于插值命令 {{}}
v-html      转义html 
v-bind      将属性 attribute 或 prop 动态绑定到表达式，缩写为 :

#### v-on         绑定事件  ，缩写为 @
可以加参数:
.stop  - 调用 event.stopPropagation()  停止冒泡
.prevent   -  调用 event.preventDefault   阻止默认行为



## Vue对象

- el (用来绑定模板 )
- data (绑定响应式数据)
- methods
- 生命周期函数 

| 生命周期函数  | 说明                                     |
|---------------|------------------------------------------|
| beforeCreate  | 在实例初始化后，事件配置前被调用         |
| created       | 在实例被创建后立即被调用                 |
| beforeMount   | 在挂载之前被调用，相关渲染函数首次被调用 |
| mounted       | 元素挂载时执行                           |
| beforeUpdate  | 数据更新时被调用                         |
| updated       | 组件 DOM 已经更新，组件更新完毕          |
| beforeDestory |                                          |
| destoryed     |                                          |


``` js
new Vue({
  el: ".app1",
  data: {
    name: "aming",
  },
  methods: {},
  created: function () {
    console.log("Vue instance has been created");
  },
  filters:{
	  upper:function(value){
		  return value.toUpperCase();
	  }
  }
});

```



## 模板
### 内容
#### 文本节点
```
{{datavar}}
```
#### html 
``` html
 <div v-html="message"></div>
```
#### 属性 
``` html
<span v-bind:style="style1">属性</span>
<div v-bind:id="'list-' + id">ID</div>
```
#### 表达式
``` html
{{5+5}}<br>
{{ ok ? 'YES' : 'NO' }}<br>
{{ message.split('').reverse().join('') }}

```

### 指令 
#### 判断
``` html
 <div v-if="type === 'A'">
      A
    </div>
    <div v-else-if="type === 'B'">
      B
    </div>
    <div v-else-if="type === 'C'">
      C
    </div>
    <div v-else>
      Not A/B/C
    </div>
```
#### 循环
``` html
<li v-for="site in sites">
      {{ site.name }}
    </li>
```

### 数据与表单形成关联
``` html
<input v-model="message">
```

v-model与 input ,select ,textarea,checkbox,radio 等表单形成关联
### 与事件属性关联 v-on
方法放在 methods 中
### 过滤filters  {{ a | b}}
### 条件 ###
#### v-if  等价于后台模板的写法 {{#if }} {{/if}} ####

#### v-else 

``` html
<div id="app">
    <div v-if="Math.random() > 0.5">
      Sorry
    </div>
    <div v-else>
      Not sorry
    </div>
</div>

```

#### 监听属性 watch 

``` html
<div id = "app">
    <p style = "font-size:25px;">计数器: {{ counter }}</p>
    <button @click = "counter++" style = "font-size:25px;">点我</button>
</div>
<script type = "text/javascript">
var vm = new Vue({
    el: '#app',
    data: {
        counter: 1
    }
});
vm.$watch('counter', function(nval, oval) {
    alert('计数器值的变化 :' + oval + ' 变为 ' + nval + '!');
});
</script>
``` 

#### 样式绑定 

##### class 

实例中将 isActive 设置为 true 显示了一个绿色的 div 块，如果设置为 false 则不显示：
``` html
<div v-bind:class="{ 'active': isActive }"></div>
``` 
用数组处理多种 class
``` html
<div v-bind:class="[errorClass ,isActive ? activeClass : '']"></div>
```

##### style

``` html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">菜鸟教程</div>
<!-- 或者绑定样式对象 -->
<div v-bind:style="styleObject">菜鸟教程</div>
```

### 事件 
#### 事件修饰符 

``` html
<!-- 阻止单击事件冒泡 -->
<a v-on:click.stop="doThis"></a>
<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>
<!-- 修饰符可以串联  -->
<a v-on:click.stop.prevent="doThat"></a>
<!-- 只有修饰符 -->
<form v-on:submit.prevent></form>
<!-- 添加事件侦听器时使用事件捕获模式 -->
<div v-on:click.capture="doThis">...</div>
<!-- 只当事件在该元素本身（而不是子元素）触发时触发回调 -->
<div v-on:click.self="doThat">...</div>

<!-- click 事件只能点击一次，2.1.4版本新增 -->
<a v-on:click.once="doThis"></a>
``` 

#### 按键修饰符

``` html
<!-- 只有在 keyCode 是 13 时调用 vm.submit() -->
<input v-on:keyup.13="submit">
记住所有的 keyCode 比较困难，所以 Vue 为最常用的按键提供了别名：
<!-- 同上 -->
<input v-on:keyup.enter="submit">
<!-- 缩写语法 -->
<input @keyup.enter="submit">
``` 
别名
```
.enter
.tab
.delete (捕获 "删除" 和 "退格" 键)
.esc
.space
.up
.down
.left
.right
.ctrl
.alt
.shift
.meta
``` 

### 声明周期函数

### 表单 v-model 双向绑定

修饰符

#### .lazy 

在默认情况下， v-model 在 input 事件中同步输入框的值与数据，但你可以添加一个修饰符 lazy ，从而转变为在 change 事件中同步：

``` html
<!-- 在 "change" 而不是 "input" 事件中更新 -->
<input v-model.lazy="msg" >
```

#### .number 

如果想自动将用户的输入值转为 Number 类型（如果原值的转换结果为 NaN 则返回原值），可以添加一个修饰符 number 给 v-model 来处理输入值：
``` html
<input v-model.number="age" type="number">
```
这通常很有用，因为在 type="number" 时 HTML 中输入的值也总是会返回字符串类型。

#### .trim 

如果要自动过滤用户输入的首尾空格，可以添加 trim 修饰符到 v-model 上过滤输入：
``` html
<input v-model.trim="msg">
```


## vue-cli
### 创建项目
``` shell
vue init webpack MY-PROJECT
cd MY-PROJECT
npm install
npm run dev
```


### file structure

- index.html     #main app file
- src/App.vue   #Component  
- src/main.js  #drive file
- src/assets/logo.png
- src/components/HelloWorld.vue   # 另一个组件，被App.vue 包含

### 添加 plugins
``` console
vue add @vue/cli-plugin-babel
```


# link
  <a :href="'addalarmnotes.do?alarmId='+item.id+'&activetype1=detail'" target="_blank">{{item.name}}</a>


## 图片的base64编码

默认是10k以下，建议都通过 base64编码。在配置文件`webpack.base.conf.js`中进行修改：

```
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('img/[name].[hash:7].[ext]')
        }
```

## 第1 章 遇见Vue.js 1
1.1 MVX 模式是什么 1
1.1.1 MVC 1
1.1.2 MVP 2
1.1.3 MVVM 3
1.2 Vue.js 是什么 4
1.2.1 Vue.js 与其他框架的区别 4
1.2.2 如何使用Vue.js 10
1.2.3 Vue.js 的发展历史 11
第2 章 数据绑定 13
2.1 语法 13
2.1.1 插值 13
2.1.2 表达式 14
2.1.3 指令 14
2.2 分隔符 15
第3 章 指令 16
3.1 内部指令 16
3.1.1 v-if 16
3.1.2 v-show 17
3.1.3 v-else 18
3.1.4 v-model 19
3.1.5 v-repeat 22
3.1.6 v-for 30
3.1.7 v-text 32
3.1.8 v-html 32
3.1.9 v-bind 33
3.1.10 v-on 34
3.1.11 v-ref 35
3.1.12 v-el 36
3.1.13 v-pre 36
3.1.14 v-cloak 36
3.2 自定义指令 37
3.2.1 基础 37
3.2.2 高级选项 41
3.3 内部指令解析 47
3.4 常见问题解析 50
第4 章 计算属性 53
4.1 什么是计算属性 53
4.2 计算属性缓存 54
4.3 常见问题 56
4.3.1 计算属性getter 不执行的场景 56
4.3.2 在v-repeat 中使用计算属性 57
第5 章 表单控件绑定 59
5.1 基本用法 59
5.1.1 text 59
5.1.2 checkbox 59
5.1.3 radio 60
5.1.4 select 60
5.2 值绑定 62
5.3 v-model 修饰指令 63
5.3.1 lazy 63
5.3.2 debounce 64
5.3.3 number 64
5.4 修饰指令原理 64
5.4.1 lazy 64
5.4.2 debounce 65
5.4.3 number 66
第6 章 过滤器 67
6.1 内置过滤器 68
6.1.1 字母操作 68
6.1.2 json 69
6.1.3 限制 69
6.1.4 currency 72
6.1.5 debounce 73
6.2 自定义过滤器 73
6.2.1 fillter 语法 73
6.2.2 教你写一个filter 75
6.3 源码解析 76
6.3.1 管道实现 76
6.3.2 过滤器解析 77
6.4 常见问题解析 78
第7 章 Class 与Style 绑定 80
7.1 绑定HTML Class 80
7.1.1 对象语法 80
7.1.2 数组语法 82
7.2 绑定内联样式 82
7.2.1 对象语法 82
7.2.2 数组语法 83
7.2.3 自动添加前缀 84
第8 章 过渡 86
8.1 CSS 过渡 87
8.1.1 内置Class 类名 88
8.1.2 自定义CSS 类名 89
8.1.3 显式声明CSS 过渡类型 89
8.1.4 动画案例 89
8.1.5 过渡流程 90
8.2 JavaScript 过渡 92
8.3 渐进过渡 93
第9 章 Method 95
9.1 如何绑定事件 95
9.1.1 内联方式 95
9.1.2 methods 配置 96
9.1.3 $events 应用 97
9.2 如何使用修饰符 97
9.2.1 prevent 98
9.2.2 stop 98
9.2.3 capture 98
9.2.4 self 98
9.2.5 按键 99
9.3 Vue.js 0.12 到1.0 中的变化 99
9.3.1 v-on 变更 99
9.3.2 @click 缩写 100
第10 章 Vue 实例方法 101
10.1 实例属性 101
10.1.1 组件树访问 101
10.1.2 DOM 访问 102
10.1.3 数据访问 102
10.2 实例方法 102
10.2.1 实例DOM 方法的使用 102
10.2.2 实例Event 方法的使用 104
第11 章 组件 107
11.1 基础 108
11.1.1 注册 108
11.1.2 数据传递 110
11.1.3 混合 123
11.1.4 动态组件 126
11.2 相关拓展 129
11.2.1 组件和v-for 129
11.2.2 编写可复用组件 130
11.2.3 异步组件 130
11.2.4 资源命名约定 131
11.2.5 内联模板 132
11.2.6 片段实例 133
11.3 生命周期 134
11.4 开发组件 136
11.4.1 基础组件 136
11.4.2 基于第三方组件开发 141
11.5 常见问题解析 146
第12 章 表单校验 154
12.1 安装 154
12.2 基本使用 155
12.3 验证结果结构 156
12.4 验证器语法 158
12.4.1 校验字段名field 158
12.4.2 校验规则定义 160
12.5 内置验证规则 163
12.5.1 required 163
12.5.2 pattern 165
12.5.3 minlength 165
12.5.4 maxlength 166
12.5.5 min 167
12.5.6 max 167
12.6 与v-model 同时使用 168
12.7 重置校验结果 169
12.8 表单元素 169
12.9 各校验状态对应的class 172
12.9.1 自定义校验状态class 173
12.9.2 在其他元素上使用校验状态class 173
12.10 分组校验 174
12.11 错误信息 174
12.11.1 错误信息输出组件 177
12.11.2 动态设置错误信息 180
12.12 事件 182
12.12.1 单个字段校验事件 182
12.12.2 整个表单校验事件 183
12.13 延迟初始化 185
12.14 自定义验证器 186
12.14.1 注册自定义验证器 187
12.15 自定义验证时机 189
12.16 异步验证 192
12.16.1 注册异步验证器 192
12.16.2 验证器函数context 194
第13 章 与服务端通信 196
13.1.1 安装 197
13.1.2 参数配置 198
13.1.3 headers 配置 199
13.1.4 基本HTTP 调用 200
13.1.5 请求选项对象 202
13.1.6 response 对象 205
13.1.7 RESTful 调用 205
13.1.8 拦截器 207
13.1.9 跨域AJAX 208
13.1.10 Promise 210
13.1.11 url 模板 211
13.2 vue-async-data 212
13.2.1 安装 212
13.2.2 使用 212
13.3 常见问题解析 213
13.3.1 如何发送JSONP 请求 213
13.3.2 如何修改发送给服务端的数据类型 215
13.3.3 跨域请求出错 215
13.3.4 $.http.post 方法变为OPTIONS 方法 216
第14 章 路由与视图 217
14.1 如何安装 217
14.2 基本使用 218
14.3 视图部分 219
14.3.1 v-link 219
14.3.2 router-view 222
14.4 路由实例 222
14.4.1 实例化路由 222
14.5 组件路由配置 227
14.5.1 路由切换的各个阶段 227
14.5.2 各阶段的钩子介绍 230
14.6 路由匹配 236
14.6.1 动态片段 236
14.6.2 全匹配片段 237
14.6.3 具名路径 237
14.6.4 路由对象 238
14.7 transition 对象 239
14.8 嵌套路由 239
14.9 动态加载路由组件 241
14.10 实战 242
14.10.1 浏览器直接引用 242
14.10.2 Webpack 模块化开发 244
14.11 常见问题解析 250
第15 章 vue-cli 254
15.1 安装 254
15.2 基本使用 254
15.3 命令 257
15.3.1 init 257
15.3.2 list 257
15.4 模板 258
15.4.1 官方模板 258
15.4.2 自定义模板 258
15.4.3 本地模板 259
15.5 不错的工具包 259
15.5.1 commander 259
15.5.2 download-git-repo 259
15.5.3 inquirer 259
15.5.4 ora 260
第16 章 测试开发与调试 261
16.1 测试工具 261
16.1.1 ESLint 261
16.1.2 工具包 263
16.2 开发工具 264
16.2.1 Vue Syntax Highlight 264
16.2.2 Snippets 264
16.2.3 其他编辑器/IDE 265
16.3 调试工具 269
第17 章 scrat+Vue.js 的化学反应 271
17.1 浅谈前端工程化 271
17.2 前端工程化怎么做 271
17.3 scrat 简介 273
17.4 scrat+Vue.js 实现组件 275
17.5 案例分析 276
17.5.1 准备工作 277
17.5.2 代码实现 279
17.5.3 编译和发布 284
17.6 总结 287
第18 章 Vue.js 2.0 288
18.1 API 变更 288
18.1.1 全局配置 288
18.1.2 全局API 289
18.1.3 VM 选项 290
18.1.4 实例属性 294
18.1.5 实例方法 294
18.1.6 指令 296
18.1.7 特殊元素 297
18.1.8 服务端渲染 297
18.2 Virtual DOM 297
18.2.1 认识Virtual DOM 297
18.2.2 Virtual DOM 在Vue.js 2.0 中的实现 299
18.3 服务端渲染技术 315
18.3.1 普通服务端渲染 315
18.3.2 流式服务端渲染 320
18.4 总结 326
第19 章 源码篇——util 327
19.1 env 327
19.1.1 系统判断 328
19.1.2 属性支持 328
19.1.3 过渡属性 329
19.1.4 nextTick 330
19.1.5 set 332
19.2 dom 332
19.2.1 dom 操作 332
19.2.2 属性操作 339
19.2.3 class 操作 341
19.2.4 事件操作 343
19.2.5 其他 344
19.3 lang 347
19.3.1 对象操作 347
19.3.2 名称转换 351
19.3.3 数组操作 352
19.3.4 类型转换 352
19.3.5 方法绑定 354
19.3.6 其他 354
19.4 components 357
19.5 options 359
19.6 debug 364
第20 章 源码篇——深入响应式原理 365
20.1 如何追踪变化 365
20.1.1 Observer 367
20.1.2 Directive 372
20.1.3 Watcher 382
20.2 变化检测问题 391
20.3 初始化数据 394
20.4 异步更新队列 395
20.5 计算属性的奥秘 398
20.6 总结 402
第21 章 源码篇——父子类合并策略 403
21.1 策略是什么 403
21.1.1 生命周期合并策略 403
21.1.2 属性方法计算 405
21.1.3 数据合并策略 406
第22 章 源码篇——缓存 409
22.1 Cache 有什么用 409
22.2 LRU 410
22.3 Cache 类 410
22.4 put 410
22.5 shift 411
22.6 get 412
第23 章 源码篇——属性props 413
23.1 流程设计 413
23.2 属性name 415
23.3 coerce 416
23.4 type 验证 416
23.5 default 417
23.6 validator 418
第24 章 源码篇——events 419
24.1 events 配置是什么 419
24.1.1 如何配置 419
24.1.2 $emit 触发 422
24.1.3 $once 绑定 424
24.1.4 $off 删除 425
24.1.5 $dispatch 派发 426
24.1.6 $broadcast 广播 427
第25 章 Webpack 428
25.1 安装 428
25.2 基本使用 429
25.3 命令行 430
25.4 配置文件 430
25.4.1 context 431
25.4.2 entry 431
25.4.3 output 432
25.4.4 module 433
25.4.5 resolve 434
25.4.6 devServer 435
25.5 开发调试 435
25.5.1 安装 435
25.5.2 启动服务 435
25.5.3 命令行参数 436
25.5.4 配置文件 436
25.6 使用插件 436
25.6.1 安装 437
25.6.2 常用插件 438
第26 章 Rollup 440
26.1 简介 440
26.2 安装 441
26.3 配置 441
26.4 命令 443
26.5 插件 447
26.6 常见问题解析 449
第27 章 Browserify 450
27.1 安装 450
27.2 基本使用 450
27.3 转换模块 451
27.3.1 安装转换模块 451
27.3.2 使用转换模块 452
27.3.3 相关转换模块介绍 452
第28 章 vue-loader 456
28.1 如何配置 456
28.2 包含内容 456
28.3 特性介绍 457
28.4 常见问题解析 458
28.5 源码解析 459
28.6 工具包介绍 465
第29 章 PostCSS 467
29.1 安装 467
29.2 配置 467
29.3 命令 468
29.4 插件 471
第30 章 拓展篇 473
30.1 Composition Event 473
30.2 ES 6 474
30.2.1 模块 475
30.2.2 let 479
30.2.3 const 481
30.3 object 482
30.4 函数柯里化 488
30.4.1 动态创建函数 488
30.4.2 参数复用 489
