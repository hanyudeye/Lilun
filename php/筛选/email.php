<?php
// 1. 邮件过滤，并不完善
$email="hellowold";
// $email = '东西是我的hello 青 发生地 john@example.com';
// echo filter_var($email,FILTER_SANITIZE_EMAIL);


// 2.html文本过滤
$html= '<p><script>alert("bad\'\"你号");</script></p>';
// echo htmlentities($html,ENT_QUOTES,'utf-8');
// 返回;p&gt;&lt;script&gt;alert(&quot;bad&#039;\&quot;你号&quot;);&lt;/script&gt;&lt;/p&gt;


//http 筛选
$pattern="/^(http:\/\/)?([^\/]+)/i";

if(preg_grep($pattern,["http://www.php.net/index.html"],0)){
    echo "匹配";
}else{
    echo "不匹配";
}