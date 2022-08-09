<?php

namespace app\api\controller;

use app\BaseController;

class File extends BaseController
{
    public function index()
    {
        return '<style type="text/css">*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }</style><div style="padding: 24px 48px;"> <h1>:) </h1><p> ThinkPHP V' . \think\facade\App::version() . '<br/><span style="font-size:30px;">14载初心不改 - 你值得信赖的PHP框架</span></p><span style="font-size:25px;">[ V6.0 版本由 <a href="https://www.yisu.com/" target="yisu">亿速云</a> 独家赞助发布 ]</span></div><script type="text/javascript" src="https://tajs.qq.com/stats?sId=64890268" charset="UTF-8"></script><script type="text/javascript" src="https://e.topthink.com/Public/static/client.js"></script><think id="ee9b1aa918103c4fc"></think>';
    }

    //上传文件 ，多文件上传
    public function upload()
    {

        // 获取表单上传文件
        $files = request()->file("file");
        // print_r($files);
        // die();

        try {
            $savename = [];
            foreach ($files as $file) {
                $savename[] = \think\facade\Filesystem::disk('public')->putFile('api', $file);
            }

            // print_r($savename);
            // die();

            return json_encode(["path" => $savename]);
        } catch (\think\exception\ValidateException $e) {
            echo $e->getMessage();
        }
    }

    //上传图片
    public function uploadImage()
    {
        // 获取表单上传文件 例如上传了001.jpg
        $file = request()->file('image');

        //验证, $file 需要 数组
        // validate(['image' => 'fileSize:100240|fileExt:jpg,png'])->check($file);
        // 上传到本地服务器
        $savename = \think\facade\Filesystem::disk('public')->putFile('api', $file);

        // return ["path" => $savename];
        return json_encode(["path" => $savename]);
        // print_r($savename);die();

    }
}
