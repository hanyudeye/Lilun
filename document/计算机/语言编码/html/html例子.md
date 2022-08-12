
# 例子
## google 查找

``` html
<form method="get" action="http://www.google.com/search">
<input type="text" name="q" placeholder="search">
</form>
```

# 图片上传
``` js
  function bjimg(i) {
            // var obj = i[0].files[0];
            // i.prev().attr("src", URL.createObjectURL(obj));
            // 

            // console.log(formdata);return;
            // console.log(i[0].files)
            // return;
            // i.prev().attr("src", data.data.url);

            let formdata = new FormData();
            formdata.append('file', i[0].files[0]);
            //图片上传
            $.ajax({
                url: '/index/ajax/upload.html',
                type: 'POST',
                cache: false,
                data: formdata,
                processData: false,
                contentType: false,
                success: function (data) {
                    if (data.code == 1) {
                        i.next().val(data.data.url)
                        i.prev().prev().attr("src", data.data.url)
                    } else {
                        alert(data.msg)
                        i.prev().prev().attr("src", '')
                    }

                }
            });
        }
```
``` php
    //上传图片
    public function upload(){
        $file = request()->file('file');
        $info = $file->move('uploads');
        if($info) {
            $data['code'] = 0;
            $data['msg'] = '/uploads/'.$info->getSaveName();

        }else{

            $data['code'] = 1;

            $data['msg'] = $file->getError();

        }
            return json($data);
    }
```

# 文件上传

```  html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name=""  id="" accept="image/*" >

```
上传类型
- audio 音频，视频
- text 文本
- image 图像
- application 其它应用格式

| 文件类型 | accept                 |
|----------+------------------------|
| *.3gpp   | audio/3gpp, video/3gpp |
| .ac3     | audio/ac3              |
| .mp3     | audio/mpeg             |
| .mp4     | audio/mp4, video/mp4   |
| .css     | text/css               |
| .csv     | text/csv               |
| .jpeg    | image/jpeg             |

#### 表单限制
##### input number类型 长度限制
``` html
<input type="number" oninput="if(value.length>5)value=value.slice(0,5)">
```

##### 限制input输入框只能输入数字

``` html
<input type="text" oninput="value=value.replace(/[^\d]/g,'')">
``` 

##### 手机号码输入验证
``` js
 function isPhoneNum(str) {
                return /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/.test(str)
            }
            
            
            
if ($('#phone').val()!="") 
{
 var Phonenumber = $('#phone').val();
   if (!isPhoneNum(Phonenumber))
   {
       layer.msg("手机号码输入不正确！")
       $('#phone').focus();
       return false;
   };       
}
```
``` html
<input type="number" class="input-text radius size-MINI" style="width:120px" id="phone" name="phone" >

```

## 表单处理

自动清空属性值

```html
		<input type="text" value="姓名" onfocus="this.value = '';"
		onblur="if (this.value == '') {this.value = '姓名';}" />
```

## 阻止表单的默认提交事件
表单提交按钮，即使 action为空，也会跳转到自己的页面

如果想要阻止表单默认提交事件，有以下几种方法：

1. 将 <input> 的 type="submit" 改为 type="button"
2. 将 <button> 的 type="submit" 改为 type="button"
3. 利用 preventDefault方法

```html
<script>
        function func(event){
            event.preventDefault();
        }
    </script>

 <form action="">
        <input type="submit" value="button" onclick="func(event)" /> 
    </form>
```

4. 使用 return false 阻止提交事件
```html
onclick="return true" 为默认的表单提交事件
onclick="return false"为阻止表单提交事件
```

5. 使用表单的 onsubmit 事件
```html
<script>
        function func(){
            return false;
        }
    </script>
 <form action="" onsubmit="return func()">

```