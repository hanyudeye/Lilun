<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use app\Request as AppRequest;
use Illuminate\Http\Request;
use Illuminate\Support\Facedes\Storage;

class AdminController extends Controller
{
    //
    public function index()
    {
        return view('Admin/login');
    }


    public function login(Request $request)
    {
        $username = $request->input('username');
        $password = $request->input('password');

        if ($username != null && $password != null) {
            $user = DB::table('admin_user')->where('username', $username)
                ->where('password', $password)->first();

            if ($user) {
                $request->session()->put('user', $user);
                return redirect('Admin/index');
            } else {
                return view('Public/error', ['title' => "密码错误", 'message' => "你输错密码了"]);
            }
        } else {
            return view('Public/error', ['title' => "输入为空", 'message' => "请输入用户名与密码"]);
        }
    }

    //主页显示
    public function aIndex(Request $request)
    {
        if ($this->checkUserIsLogin($request)) {
            return view('Admin/index');
        } else {
            return redirect('../');
        }
    }

    //检测是否登录
    public function checkUserIsLogin(Request $request)
    {
        //
        $value = $request->session()->get('user');
        if ($value != '') {
            return true;
        } else {
            return false;
        }
    }
}
