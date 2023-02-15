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

## 组件

Basic
Layout 布局
Container 布局容器

<el-container>：外层容器。当子元素中包含 <el-header> 或 <el-footer> 时，全部子元素会垂直上下排列，否则会水平左右排列。

<el-header>：顶栏容器。

<el-aside>：侧边栏容器。

<el-main>：主要区域容器。

<el-footer>：底栏容器。

Color 色彩
Typography 字体
Border 边框
Icon 图标
Button 按钮
Link 文字链接
Form
Radio 单选框
Checkbox 多选框
Input 输入框
InputNumber 计数器
Select 选择器
Cascader 级联选择器
Switch 开关
Slider 滑块
TimePicker 时间选择器
DatePicker 日期选择器
DateTimePicker 日期时间选择器
Upload 上传
Rate 评分
ColorPicker 颜色选择器
Transfer 穿梭框
Form 表单
Data
Table 表格
Tag 标签
Progress 进度条
Tree 树形控件
Pagination 分页
Badge 标记
Avatar 头像
Notice
Alert 警告
Loading 加载
Message 消息提示
MessageBox 弹框
Notification 通知
Navigation
NavMenu 导航菜单
Tabs 标签页
Breadcrumb 面包屑
PageHeader 页头
Dropdown 下拉菜单
Steps 步骤条
Others
Dialog 对话框
Tooltip 文字提示
Popover 弹出框
Popconfirm 气泡确认框
Card 卡片
Carousel 走马灯
Collapse 折叠面板
Timeline 时间线
Divider 分割线
Calendar 日历
Image 图片
Backtop 回到顶部
InfiniteScroll 无限滚动
Drawer 抽屉