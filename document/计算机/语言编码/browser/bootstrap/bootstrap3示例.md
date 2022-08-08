### bootstrap3  confirm

### 验证身份证和手机号

``` html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>首页</title>
    <link rel="shortcut icon" href="img/favicon.ico">
    <link rel="apple-touch-icon" href="img/favicon.ico">
    <link href="https://cdn.bootcss.com/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
     <link href="http://cdn.bootcss.com/bootstrap-validator/0.5.3/css/bootstrapValidator.min.css" rel="stylesheet" />  

</head>

<body> 
    <form class="" autocomplete="off">
        <div class="form-group">
            <label>姓名</label>
            <input type="text" class="form-control" name="name" />
        </div>
        <div class="form-group">
            <label>身份证号</label>
            <input type="text" class="form-control" name="identity" />
        </div>
        <div class="form-group">
            <label>手机号</label>
            <input type="text" class="form-control" name="tel" />
        </div>
        <div class="form-group">
            <button type="button" id="submit" name="submit" class="btn btn-primary">提交</button>
            <button type="button" id="reset" name="reset" class="btn btn-primary">重置</button>
        </div>
    </form> 
 

    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="http://cdn.bootcss.com/bootstrap-validator/0.5.3/js/bootstrapValidator.min.js"></script> 
    <script>
        $('form').bootstrapValidator({
            message: 'This value is not valid',
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                name: {
                    message: '用户名验证失败',
                    validators: {
                        notEmpty: {
                            message: '用户名不能为空'
                        },
                        stringLength: {
                            min: 4,
                            message: '用户名长度必须大于4个字符'
                        },
                    }
                },
                identity: {
                    validators: {
                        notEmpty: {
                            message: '身份证号码不能为空'
                        },
                        callback: {
                            message: '身份证号码格式错误',
                            callback: function (value, validator) {
                                if (!value) {
                                    return true
                                } else if (isCardNo(value)) {
                                    return true;
                                } else {
                                    return false;
                                }
                            }
                        }
                    }
                },
                tel: {
                    validators: {
                        notEmpty: {
                            message: '手机号不能为空'
                        },
                        regexp: {
                            regexp: /^1\d{10}$/,
                            message: '手机号格式错误'
                        }
                    }
                }
            }
        });

        var bootstrapValidator = $('form').data('bootstrapValidator');

        // 提交时验证
        $('#submit').on('click', function () {
            bootstrapValidator.validate();
            if (bootstrapValidator.isValid()) {
                //表单提交的方法、比如ajax提交
                alert('success');
            }
        })

        // 重置表单
        $('#reset').on('click', function () {
            bootstrapValidator.resetForm();
            $('input').val('')
        }) 
        
        // 验证身份证号
        function isCardNo(card) {
            let reg = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
            if (reg.test(card) === false) {
                return false
            } else {
                return true
            }
        }
        
        // 验证手机号
        function checkMobile(str) {
            let re = /^1\d{10}$/
            if (re.test(str)) {
                return true;
            } else {
                return false;
            }
        }

</script>

</body>

</html>

```
