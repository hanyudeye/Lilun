## vue3
Vue 关注 MVC 模式中的视图，做的是 视图中的数据监控，通过 mount 对象建立监听。 

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



