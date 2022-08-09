<?php

$path = "c:/aa/bb/dd\cc.tx";
echo basename($path);

getcwd();
chdir("php");

$filepath = "hello";
if (file_exists($filepath)) {
    $f = fopen($filepath, "a+");
    fwrite($f, "nihao\n");
    fclose($f);
}
