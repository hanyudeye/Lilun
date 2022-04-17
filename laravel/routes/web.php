<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\Admin\AdminController;
use App\Http\Controllers\Admin\TestController;;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/xxx', function () {
    // return view('welcome');
    echo "ffo";
});

//API 获取所有书的列表
Route::get('API/', 'Text\TextController@index');
//API 用户注册
Route::post('API/register', 'Text\TextController@register');
//管理登录界面
Route::get('API/', 'Text\TextController@index');
//管理员

Route::get('/', 'App\Http\Controllers\Admin\AdminController@index');
// Route::get('/', [AdminController::class, "index"]);

// Route::get('/', [TestController::class, "index"]);
