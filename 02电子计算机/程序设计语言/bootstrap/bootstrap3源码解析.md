#### 排版与链接

bootstrap 内置了基本的全局样式，可以在 scaffolding.less 找到相应的源码。

1. 为body 元素设置 background-color:#fff;
2. 为所有链接设置基本颜色 @link-color,并且 :hover 时有下划线。

#### 媒体查询 (有条件的CSS规则)
``` css
/* 超小设备（手机，小于 768px） */
/* 在Bootstrap中默认情况下没有媒体查询 */

/* 小型设备（平板电脑，768px 起） */
@media (min-width: @screen-sm-min) { ... }

/* 中型设备（台式电脑，992px 起） */
@media (min-width: @screen-md-min) { ... }

/* 大型设备（大台式电脑，1200px 起） */
@media (min-width: @screen-lg-min) { ... }

```
