<?php

include_once("math/Add.php");

use math;

class test
{
    public function index()
    {
        $m = new math\Add();
        $m->toString();
    }

}

$t=new test();
$t->index();

// echo intval('10',16);
$a=['name'=>"i希奥利",'age'=>99];
$b=['name'=>"几个",'age'=>89];

$c=array_diff($a,$b); 
// print_r($c);
$d=array_keys($a);
print_r($d);