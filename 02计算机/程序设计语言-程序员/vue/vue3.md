## vue3

### CDN
``` html
<script src="https://unpkg.com/vue@next" rel="external nofollow" ></script>
```

### npm

``` sh
# 最新稳定版
$ npm install vue@next
```

### cli
```sh
npm install -g @vue/cli@next
```

### 运行时+编译器 vs 仅运行时

如果需要在客户端上编译模板（即：将字符串传递给template选项），你需要编译器，因此需要完整的版本

```js

// 需要编译器
Vue.createApp({
    template:'<div>{{h1}}</div>'
})

//不需要
// 不需要
Vue.createApp({
  render() {
    return Vue.h('div', {}, this.hi)
  }
})

```
当使用 vue-loader 时， *.vue 文件中的模板在生成时预编译为 JavaScript，在最终的打包器中并不需要编译器，因此可以只使用运行时构建。


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