<?php

//  1
echo is_numeric(3);
echo  '---';

// 2
echo is_string('3');
echo  '---';

class A{}
// 3
echo is_object(new A());
echo  '---';

// 4
$b=new A();
echo isset($b);
echo  '---';

//5
echo empty($b);
echo  '---';

echo doubleval("323.21");
