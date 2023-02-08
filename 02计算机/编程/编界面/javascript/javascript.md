## javascript

    

## 事件

### 鼠标事件

| 名称                | 含义 |
|---------------------|------|
| window.onmousewheel | 滚轮 |

### 键盘事件

## jquery 防止重复点击提交

### 方法二： 使用 jquery 中 one() 方法

同样是上面 Html 例子，也是只可点击一次；再次点击需要页面重新进行了加载或者跳转；该方式是将绑定 on 方法 改为 one 方法 ，如下：

    ```js
        $(function(){
            $('#submitBtn').one('click‘，function(){
                    $(this).attr('disabled',true); //点击后就禁用，若想再次点击需刷新页面；
                    $(this).val('登录中...');  //此处设置 value 值给以提示
                    this.form.submit();
            });
        });
```

### 方法三： 针对 ajax 请求方式

异步请求更好的适应用户的体验，为防止多次提交，可在提交前做处理；

```js
     $(function () {
        $('#submitBtn').click(function () {
            //1.先进行表单验证
            //......
            //2.异步提交
            $.ajax({
                url: url+'/login',
                data: $('form').serialize(),
                type: 'post',
                beforeSend: function () {
                    //3.设置提交按钮失效，以实现防止按钮重复点击
                    $(this).attr('disabled', true);
                    //4.给用户提示
                    $(this).val('登录中...');
                },
                complete: function () {
                    //5.提交完成后按钮重新设置有效
                    $(this).removeAttr('disabled');
                },
                success: function(data){
                    if (data === 'ok') {
                        alert('登录成功！');
                        //做逻辑处理
                        //......
                    } else {
                        alert('登录失败，请重新登录！');
                    }
                }
            }); 
        });
    });
```

