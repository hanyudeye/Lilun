# 代码片段

## FormData使用方法详解

FormData的主要用途有两个：
1、将form表单元素的name与value进行组合，实现表单数据的序列化，从而减少表单元素的拼接，提高工作效率。
2、异步上传文件

### 一、创建formData对象
1、创建一个空对象：
``` js
//通过FormData构造函数创建一个空对象
var formdata=new FormData();
//可以通过append()方法来追加数据
formdata.append("name","laotie");
//通过get方法对值进行读取
console.log(formdata.get("name"));//laotie
//通过set方法对值进行设置
formdata.set("name","laoliu");
console.log(formdata.get("name"));//laoliu
```

2、通过表单对formData进行初始化
创建表单：
``` html
<form id="advForm">
    <p>广告名称：<input type="text" name="advName"  value="xixi"></p>
    <p>广告类别：<select name="advType">
        <option value="1">轮播图</option>
        <option value="2">轮播图底部广告</option>
        <option value="3">热门回收广告</option>
        <option value="4">优品精选广告</option>
    </select></p>
    <p><input type="button" id="btn" value="添加"></p>
</form>
```
通过表单元素作为参数，实现对formData的初始化：

``` js
//获得表单按钮元素
var btn=document.querySelector("#btn");
//为按钮添加点击事件
btn.onclick=function(){
    //根据ID获得页面当中的form表单元素
    var form=document.querySelector("#advForm");
    //将获得的表单元素作为参数，对formData进行初始化
    var formdata=new FormData(form);
    //通过get方法获得name为advName元素的value值
    console.log(formdata.get("advName"));//xixi
    //通过get方法获得name为advType元素的value值
    console.log(formdata.get("advType"));//1 
}
```

## 置顶
``` html
<a href="javascript:;" onclick="$('html,body').animate({scrollTop: '0px'}, 800)" class="btn_top">TOP ↑</a>
```
