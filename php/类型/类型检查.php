<?php

$obj1=123;
echo $obj1;
echo gettype($obj1);
settype($obj1,"string");
echo $obj1."helo";
echo gettype($obj1);


echo doubleval("23.12311");
echo strval(32.5123)+1;