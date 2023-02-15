## elementui

### 安装
```
npm install element-ui -S
 ```

## sass
```
npm install sass-loader@7.3.1 node-sass --save-dev
```

### 引入
``` js
import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';

Vue.use(ElementUI);

new Vue({
  el: '#app',
  render: h => h(App)
});
```

