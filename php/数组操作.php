<?php

$student=['张三','李四','王五'];
echo $student[1];

$大小键数组=[
    'a'=>'aval',
    'B'=>'Bval',
    'c'=>'Cval'
];

//把数组的键改为大/小写
$a=array_change_key_case($大小键数组,CASE_UPPER);
// print_r($a);
echo $a['a'];  // 小写就没有值了

// 数组分割
$b=array_chunk($student,1);
// print_r($b);

$c=[1,2,3];
$d=[3,2,"5","hello"];
// $d=[4,6];
// 没法合并
// print_r($c+$d);
//合并数组
// print_r(array_merge($student,$c,$d));
//比较数组，打印相同的
// print_r(array_diff($c,$d));

function add1($v){
    return $v+1;
}

//映射
// print_r(array_map('add1',$c));

$e=[3,2,'1',"9"];
//升序
sort($e);
// print_r($e);

//降序
rsort($e);
// print_r($e);

$f=["name"=>"a","age"=>99];
print_r(current($f));
print_r(next($f));
