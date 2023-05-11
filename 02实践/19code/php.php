<?php

// 判断是否存在指定字符串
function strExisted($haystack, $needle)
{
    return !strpos($haystack, $needle) === false;
}

// echo strExisted("hello","el");
// echo strExisted("hello","lel")==false?"no":"yes";

class Index
{

    public function __initialize()
    {
        $agent = $_SERVER['HTTP_USER_AGENT'];

        if (!strpos($agent, "icroMessenger")) {
            echo '此功能需要在微信浏览器中使用';
            exit;
        }

        $this->token = md5("bababa");

    }
}
