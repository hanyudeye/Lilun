https://24kcs.github.io

## vue3
Vue 关注 MVC 模式中的视图，做的是 视图中的数据监控，通过 mount 对象建立监听。 

- 组件 将大型应用程序切割成独立、复用的组件

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

官方库
- Vue Router: 允许开发者编写在多个视图中切换的单网页应用程序
- Vue Server Render: Vue.js 的服务器端渲染(SSR)

### npm
- 安装
``` sh
# 最新版
$ npm init vue@latest
```
- npm install
- npm run dev
- npm run build

# 声明式渲染

```html
<div id="counter">
  Counter: {{ counter }}
</div>
```

```js
const Counter = {
  data() {
    return {
      counter: 0
    }
  }
}
Vue.createApp(Counter).mount('#counter')
```

## 获取数据



