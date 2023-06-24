---
title: vue2
permalink: .html
theme: jekyll-theme-cayman
---

https://github.com/hardphp/tp6-vue-admin.git
https://github.com/icarusion/vue-book
https://github.com/sg552/happy_book_vuejs.git


Vue.js是一款轻量级、易上手的JavaScript框架，它可以帮助开发人员快速构建交互式Web应用程序。

## 开发模式的演化(前后端分离)

 前后端的分离，有助于大项目的团队协助，就不用做全栈了。

## 对象

- el (用来绑定模板 )
- data
- methods
- 生命周期 created mounted(元素挂载时执行) updated,beforeDestory,destoryed


``` js
new Vue({
  el: ".app1",
  data: {
    name: "aming",
  ,
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

#### 监听属性 watch ####

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

#### 样式绑定 ####

##### class #####

实例中将 isActive 设置为 true 显示了一个绿色的 div 块，如果设置为 false 则不显示：
``` html
<div v-bind:class="{ 'active': isActive }"></div>
``` 
用数组处理多种 class
``` html
<div v-bind:class="[errorClass ,isActive ? activeClass : '']"></div>
```

##### style #####

``` html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">菜鸟教程</div>
<!-- 或者绑定样式对象 -->
<div v-bind:style="styleObject">菜鸟教程</div>
```

### 事件 ###
#### 事件修饰符 ####

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

#### 按键修饰符 ####

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


### 表单 v-model 双向绑定 ###

修饰符

#### .lazy ####

``` html
<!-- 在 "change" 而不是 "input" 事件中更新 -->
<input v-model.lazy="msg" >
```

#### .number ####

如果想自动将用户的输入值转为 Number 类型（如果原值的转换结果为 NaN 则返回原值），可以添加一个修饰符 number 给 v-model 来处理输入值：
``` html
<input v-model.number="age" type="number">
```
这通常很有用，因为在 type="number" 时 HTML 中输入的值也总是会返回字符串类型。

#### .trim ####

如果要自动过滤用户输入的首尾空格，可以添加 trim 修饰符到 v-model 上过滤输入：
``` html
<input v-model.trim="msg">
```


# link
  <a :href="'addalarmnotes.do?alarmId='+item.id+'&activetype1=detail'" target="_blank">{{item.name}}</a>

# Vue.js
## 组件
``` js
// 定义一个名为 button-counter 的新组件
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
```

## 模板

jsx 语法 
``` jsx
Vue.component('buttonclicked', {
  props: ["initial_count"],
  data: function() {var q = {"count": 0}; return q;} ,
  render: function (h) {
    return (<button vOn:click={this.onclick}>Clicked {this.count} times</button>)
  },
  methods: {
    "onclick": function() {
      this.count = this.count + 1;
    }
  },
  mounted: function() {
    this.count = this.initial_count;
  }
});

```
## vue-router 页面跳转

- 安装  npm install vue-router --save-dev


### 安装Vue

你可以使用CDN链接来安装Vue.js:

```
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
```

如果你想下载并本地安装Vue.js，可以通过npm或yarn来完成：

```
npm install vue
或
yarn add vue
```

### 创建Vue实例

你可以通过创建Vue实例来启动Vue应用程序，它是Vue.js的核心。

```
var app = new Vue({
  el:'#app',
  data:{
    message: 'Hello Vue!'
  }
})
```

在上面的代码中，我们创建了一个Vue实例，并将其挂载到id为"app"的元素上。我们还定义了一个data属性，用于存储应用程序中的数据，例如"message"属性。

### 使用指令

Vue.js中的指令是一种特殊的HTML属性，用于更改元素的行为或外观。以下是一些常用的指令：

* v-text：将元素内容替换为Vue实例中指定的数据。

* v-html：将元素内容替换为Vue实例中指定的HTML代码。

* v-show：根据指定的表达式来切换元素的可见性。

* v-if：根据指定的表达式来添加或删除元素。

* v-for：根据指定的数据数组来循环渲染元素。

* v-on：用于绑定事件处理程序，例如@click表示点击事件。

以下是一个简单的例子：

```
<div id="app">
  <p v-text="message"></p>
  <button v-on:click="changeMessage">Change message</button>
</div>

<script>
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  },
  methods: {
    changeMessage: function () {
      this.message = 'Message changed!'
    }
  }
})
</script>
```

在上面的代码中，我们使用v-text指令将元素内容替换为Vue实例中的数据，并使用v-on指令来绑定一个点击事件处理程序。

### 使用组件

Vue.js中的组件是一种可重复使用、独立功能的定义。你可以通过Vue.component()方法来创建新的组件。

以下是一个简单的例子：

```
<template id="hello-component">
  <div>
    <p>Hello Vue.js!</p>
  </div>
</template>

<script>
Vue.component('hello', {
  template: '#hello-component'
})

var app = new Vue({
  el: '#app',
})
</script>

<div id="app">
  <hello></hello>
</div>
```

在上面的代码中，我们创建了一个名为"hello"的组件，并在模板中定义了其结构和功能。我们还将其组件挂载到id为"app"的元素上，并在HTML中使用组件标签"helloworld"来渲染组件。

### 使用路由

Vue.js中的路由，允许你在应用程序中定义不同的URL地址，并关联到不同的组件。

以下是一个简单的例子：

```
<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>

<div id="app">
  <router-view></router-view>
</div>

<script>
var Home = { template: '<div><h1>Home</h1></div>' }
var About = { template: '<div><h1>About</h1></div>' }

var routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]

var router = new VueRouter({
  routes: routes
})

var app = new Vue({
  router: router
}).$mount('#app')
</script>
```

在上面的代码中，我们使用VueRouter创建了一个路由实例，并定义了不同的URL地址和相关组件。我们还将其路由挂载到Vue实例中，并使用$mount()方法将Vue实例挂载到id为"app"的元素上。

以上是Vue.js 2.x的详细教程，希望对你有所帮助！