---
title: Html网页
permalink: html2learn.html
theme: jekyll-theme-cayman
---

> 超级文本，用来显示 图型页面


# 定义页面
- 定义页面类型  <!DOCTYPE html> 
- 定义整个页面的包裹根元素 <html> 
- 定义头部区  <head> 
- 定义文档的标题<title> 
- 定义文档的内容区 <body> 
- 定义脚本 <script> 
- 定义页面样式 <style>  
- 定义小favicon <link rel="shortcut icon" href="/img/favicon.ico" />
- 定义显示接口  <meta name="viewport" content="width=device-width, initial-scale=1.0">

- 定义其它属性 <meta> (变化)  
 - <meta charset="utf-8"> 声明编码，当网页文件编码错误的时候，按此可以纠正浏览器渲染的编码  <meta charset="ascii"> 美国标准码

# 定义页面内容 <body> 区

## 定义结构 

- 定义导航 nav 
- 定义区块  section 
- 定义头部 header 
- 定义正文 article 
- 定义补充 aside 用以表达注记、贴士、测栏、摘要、引用等作为补充主体的内容。如侧边栏或摘要
- 定义元素细节 details
- 定义对话框或窗口  dialog
- 为 details 定义可见标题 summary
- 定义尾部 footer 
- figure 是对多个标签进行组合并展示，通常与 figcaption联合使用
- 定义水平线 <hr>

## 定义具体内容

### 定义文字

- 定义引用 blockquote    
- 定义上下标  sup  sub 
- 定义删除线 del s   

### 特殊字符，用特定的标识替换

| 特殊字符 | 描述           | 字符的代码 |
|:---------|:---------------|:-----------|
|          | 空格符         | `&nbsp;`   |
| <        | 小于号         | `&lt;`     |
| >        | 大于号         | `&gt;`     |
| &        | 和号           | `&amp;`    |
| ￥       | 人民币         | `&yen;`    |
| ©        | 版权           | `&copy;`   |
| ®        | 注册商标       | `&reg;`    |
| °       | 摄氏度         | `&deg;`    |
| ±       | 正负号         | `&plusmn;` |
| ×       | 乘号           | `&times;`  |
| ÷       | 除号           | `&divide;` |
| ²        | 平方2（上标2） | `&sup2;`   |
| ³        | 立方3（上标3） | `&sup3;`   |

### 定义图像 img
### 定义表格 table
``` html
<table border="" cepadding="" cellspacing="">
    <thead>
        <tr>
            <th colspan=""></th>
            <th rowspan></th>
        </tr>
    </thead>
    <tfoot>
        <tr>
            <td ></td>
            <td></td>
        </tr>
    </tfoot>
    <tbody align="">
        <tr>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

```

- colspan 单元格跨列
- rowspan 单元格跨行

## 定义表单

<form action="" id=""form_id" name="form_name" method="" autocomplete enctype="">
- action 提交到的服务端地址
- method 指定提交时用哪种HTTP方法：POST或GET
- autocomplete="on/off" 浏览器是否可以自动填充(历史记录填充)
- enctype 指定表单内容编码
   - application/x-www-form-urlencoded  
   - multipart/form-data   (含有文件的表单)
- pattern="[a-zA-Z0-9]*"  输入限制

input type
- text 文本输入
- tel 电话
- password 密码
- radio 单选
- checkbox 多选
- number 数字
- 小数  `<input type="number" min="0" max="100" step="0.01"/>`
- date 日期
- color 色彩
- range 范围  max min
- email 邮件
- url 
- file 文件  multiple
- button 按钮
- submit 提交按钮

select option  下拉
textarea  文本域

``` html
 <input type="radio" id="huey" name="drone" value="huey" checked>
```

## 定义多媒体
### audio
``` html
<audio controls>
<source src="song.ogg">
<source src="song.mp3">
</audio>
```

``` js
let audio =$('audio')
audio.currentPosition;  //得到要播放的位置
audio.play(); //播放
audio.volume //获取音量

```

### video
>仅支持 mp4 H.264, webm和 Ogg 

``` js
<video controls id="v">
	<source src="a.mp4">
</video>
```
- autoplay 自动播放
- autobuffer 自动缓冲
- loop 循环

