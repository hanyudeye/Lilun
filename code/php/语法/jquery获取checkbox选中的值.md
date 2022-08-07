```html
<input type="checkbox" name="xpz" value="1"/>苹果 
<input type="checkbox" name="xpz" value="2"/>橘子 
<input type="checkbox" name="xpz" value="3"/>梨子 
<input type="checkbox" name="xpz" value="4"/>香蕉
<br/><br/>
<input type="button" id="btn1" value="全选"> 
<input type="button" id="btn2" value="取消全选"> 
<input type="button" id="btn3" value="选中所有奇数"> 
<input type="button" id="btn4" value="反选"> 
<input type="button" id="btn5" value="获得选中的所有值"> 
```

```js
$("#btn1").on("click",function(){
	$("[name='xpz']").prop("checked",'checked');//全选 
});
 
$("#btn2").on("click",function(){ 
	$("[name='xpz']").removeAttr("checked");//取消全选 
}) 
$("#btn3").click(function(){ 
	$("[name='xpz']:even").prop("checked",'true');//选中所有奇数 
}) 
$("#btn4").click(function(){ 
	$("[name='xpz']").each(function(){ 
		this.checked=!this.checked;
	}) 
}) 
$("#btn5").click(function(){ 
	var chk_value =[];//定义一个数组
	$('input[name="xpz"]:checked').each(function(){//遍历每一个名字为nodes的复选框，其中选中的执行函数
		chk_value.push($(this).val());//将选中的值添加到数组chk_value中
	});
	var selectId = chk_value.join(",");
	alert(selectId);
}) 
```