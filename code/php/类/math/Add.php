<?php
namespace math;

class Add{
    public function __construct(){
        $this->classname="add";
    }

    public function toString(){
        echo "类名是".$this->classname;
    }
}