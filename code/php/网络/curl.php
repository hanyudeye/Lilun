<?php

$c = curl_init();
curl_setopt($c, CURLOPT_URL, "http://example.com/");
// 获取数据
curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);

$a = curl_exec($c);
if (!$a) {
    trigger_error(curl_error($c));
} else {
    print_r($a);
}

curl_close($c);
