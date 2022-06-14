<?php

namespace Earth;

// 动物
class Animal
{

    //包含的动物
    public    $Animals = ["niu", "yang", "zhu", "gou"];

    public function show()
    {
        print_r($this->Animals);
    }
}
