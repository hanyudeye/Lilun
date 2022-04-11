<?php

require_once( '轮子.php');

class 汽车 extends 轮子{
    public function 直行(){
        echo "汽车直行";
    }
}

$car=new 汽车();
$car->直行();