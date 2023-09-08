---
title: ThinkPHP5.0完全开发手册
permalink: thinkphp5.html
theme: jekyll-theme-cayman
---

## 简介

ThinkPHP是 网页内容 服务框架。

行为：入口(请求) -> 转到应用 -> 判断模块 -> 调用控制器 -> 执行操作 -> 连接模型 -> 视图组装 -> 响应输出

<!--more-->

## 配置

``` php
 // 获取配置
    dump(config('database.hostname'));
    // 用'?'判断配置是否存在
    dump(config('?database.hostname'));
    // 设置配置
    config('database.hostname','localhost');
    // 获取配置
    dump(config('database.hostname'));
```


## 控制器

制器文件的命名规范是 : 首字母需要大写，如果是两个单词的组合，如 HelloWorld ，则 URL 为 hello_world

## 请求处理

### 获取URL信息

``` php
$request = Request::instance();
// 获取当前域名
echo 'domain: ' . $request->domain() . '<br/>';
// 获取当前入口文件
echo 'file: ' . $request->baseFile() . '<br/>';
$request->param()
// 获取当前URL地址 不含域名
echo 'url: ' . $request->url() . '<br/>';
// 获取包含域名的完整URL地址
echo 'url with domain: ' . $request->url(true) . '<br/>';
// 获取当前URL地址 不含QUERY_STRING
echo 'url without query: ' . $request->baseUrl() . '<br/>';
// 获取URL访问的ROOT地址
echo 'root:' . $request->root() . '<br/>';
// 获取URL访问的ROOT地址
echo 'root with domain: ' . $request->root(true) . '<br/>';
// 获取URL地址中的PATH_INFO信息
echo 'pathinfo: ' . $request->pathinfo() . '<br/>';
// 获取URL地址中的PATH_INFO信息 不含后缀
echo 'pathinfo: ' . $request->path() . '<br/>';
// 获取URL地址中的后缀信息
echo 'ext: ' . $request->ext() . '<br/>';
```
### 设置/获取 模块/控制器/操作名称
```php
$request = Request::instance();
echo "当前模块名称是" . $request->module();
echo "当前控制器名称是" . $request->controller();
echo "当前操作名称是" . $request->action();
```
#### 获取请求参数
```php
$request = Request::instance();
echo '请求方法：' . $request->method() . '<br/>';
echo '资源类型：' . $request->type() . '<br/>';
echo '访问ip地址：' . $request->ip() . '<br/>';
echo '是否AJax请求：' . var_export($request->isAjax(), true) . '<br/>';
echo '请求参数：';
dump($request->param());
echo '请求参数：仅包含name';
dump($request->only(['name']));
echo '请求参数：排除name';
dump($request->except(['name']));
```
#### 获取路由和调度信息
```php
$request = Request::instance();
echo '路由信息：';
dump($request->route());
echo '调度信息：';
dump($request->dispatch());
```
#### 设置请求信息
如果某些环境下面获取的请求信息有误，可以手动设置这些信息参数，使用下面的方式：
```php
$request = Request::instance();
$request->root('index.php');
$request->pathinfo('index/index/hello');
```

### 输入变量

可以通过 Request 对象完成对全局输入变量的检测、获取和安全过滤。支持包括 $_GET、$_POST、$_REQUEST、$_SERVER、$_SESSION、$_COOKIE、$_ENV 等系统变量，以及文件上传的信息。

#### 检测变量是否设置
```php
Request::instance()->has('id','get');
Request::instance()->has('name','post');
```
或者使用助手函数
```php
input('?get.id');
input('?post.name');
```
##### 获取PARAM变量
PARAM变量是框架提供的用于自动识别 GET、POST或者PUT 请求的一种方式，系统推荐

```php
// 获取当前请求的name变量
Request::instance()->param('name');
// 获取当前请求的所有变量（经过过滤）
Request::instance()->param();
// 获取当前请求的所有变量（原始数据）
Request::instance()->param(false);
// 获取当前请求的所有变量（包含上传文件）
Request::instance()->param(true);
```
助手函数:
```php
input('param.name');
input('param.');
或者
input('name');
input('');
```

获取 cookie 或 session
```php
Request::instance()->session('user_id'); // 获取某个session变量
input('cookie.user_id');
input('cookie.');// 获取全部的cookie变量
```

#### 变量过滤
> 框架默认没有设置过滤规则，可以自己设置
```php
// 默认全局过滤方法 用逗号分隔多个
'default_filter'         => 'htmlspecialchars',
```

使用 filter方法进行过滤，支持设置多个过滤方法，例如：
```php
Request::instance()->filter(['strip_tags','htmlspecialchars']),
```

也可以在获取变量的时候添加过滤方法，如:
``` php
Request::instance()->get('name','','htmlspecialchars'); // 获取get变量 并用htmlspecialchars函数过滤
Request::instance()->param('username','','strip_tags'); // 获取param变量 并用strip_tags函数过滤
Request::instance()->post('name','','org\Filter::safeHtml'); // 获取post变量 并用org\Filter类的safeHtml方法过滤

Request::instance()->param('username','','strip_tags,strtolower'); // 获取param变量 并依次调用strip_tags、strtolower函数过滤
Request::instance()->post('email','','email');
```
#### 获取部分变量
```php
// 只获取当前请求的id和name变量
Request::instance()->only(['id','name']);
```
#### 排除部分变量
```php
// 排除GET请求的id和name变量
Request::instance()->except(['id','name'],'get');
```
#### 变量修饰符
语法：input('变量类型.变量名/修饰符');
```php
input('get.id/d');
input('post.name/s');
input('post.ids/a');
```

| 修饰符 | 作用                 |
| ------ | -------------------- |
| s      | 强制转换为字符串类型 |
| d      | 强制转换为整型类型   |
| b      | 强制转换为布尔类型   |
| a      | 强制转换为数组类型   |
| f      | 强制转换为浮点类型   |

注意：如果你要获取的数据是数组，请一定要加上 /a 修饰符

#### 更改变量
```php
// 更改GET变量
Request::instance()->get(['id'=>10]);
```
注意：param 会无效
```php
//此方法无效
Request::instance()->param(['id'=>10]);
```
### 请求类型
#### 获取请求类型
```php
// 是否为 GET 请求
if (Request::instance()->isGet()) echo "当前为 GET 请求";
```

助手函数
```php
// 是否为 GET 请求
if (request()->isGet()) echo "当前为 GET 请求";
```
### HTTP头信息
```php
$info = Request::instance()->header();
echo $info['accept'];
echo $info['accept-encoding'];
echo $info['user-agent'];
```
## 数据库

### 查询构造器 (非原生写法)

#### 查询数据

##### 基本查询
查询一个数据使用find，查询数据集使用 select;
``` php
// table方法必须指定完整的数据表名
Db::table('think_user')->where('id',1)->find();
Db::name('user')->where('id',1)->find();
```

###### 主从查询
如果你使用了分布式数据库，默认都是在从数据库进行查询，如果你在一些特殊情况下需要从主库查询，可以：
``` php
Db::name('user')->master()->where('id',1)->find();
```

如果你想处理  一旦某个表写入了数据，那么当前请求的后续查询都自动从主库读取。
可以配置:
```php
// 从主库读取数据
'read_master'	=>	true,
```
或者使用方法 readMaster
```php
$data = ['foo' => 'bar', 'bar' => 'foo'];
Db::table('think_user')
	->readMaster(true)
    ->insert($data);
// 后续所有数据表的查询都会走主库
```

###### 值和列查询
```php
// 返回某个字段的值
Db::table('think_user')->where('id',1)->value('name');
// 返回数组
Db::table('think_user')->where('status',1)->column('name');
// 指定索引
Db::table('think_user')->where('status',1)->column('name','id');
```

###### 数据集分批处理
对于大量的数据，可以考虑 chunk 方法，该方法一次获取结果集的一小块，然后填充每一小块数据到要处理的闭包，处理大量数据库记录时非常有用。

比如，我们对用户表进行分批处理，每次处理100个用户记录：

```php
Db::table('user')->chunk(100,function($users){
foreach($users as $user){
    //
}
});

//或者交给回调方法myUserIterator处理
Db::table('user')->chunk(100, 'myUserIterator');
```

可以通过在闭包函数中返回 false 来中止对数据集的处理
```php
Db::table('think_user')->chunk(100, function($users) {
    // 处理结果集...
    return false;
});
```
也支持在 chunk 方法之前调用其它查询方法。
```php
Db::table('think_user')->where('score','>',80)->chunk(100, function($users) {
```

chunk方法的处理默认是根据主键查询，但支持指定处理数据的顺序。
```php
Db::table('think_user')->chunk(100, function($users) {
    // 处理结果集...
    return false;
},'create_time', 'desc');
```
##### JSON类型数据查询

```php
// 查询JSON类型字段 （info字段为json类型）
Db::table('think_user')->where('info$.email','thinkphp@qq.com')->find();
```
#### 添加/更新/删除 数据

添加一条数据
```php
Db::name('user')->insert($data);
```

- insert / insertGetId($data) /insertAll($data)
- update/setInc('field',value,time)/setDec/
- delete

延时更新

setInc/setDec支持延时更新，如果需要延时更新则传入第三个参数
下例中延时10秒，给score字段增加1
```php
Db::table('think_user')->where('id', 1)->setInc('score', 1, 10);
```

删除数据
```php
// 根据主键删除
Db::table('think_user')->delete(1);
// 条件删除    
Db::table('think_user')->where('id',1)->delete();
```
### 查询方法
#### 条件查询 where 与 whereOr
``` php
->where('name&title','like','%thinkphp')
->whereOr('title','like','%thinkphp')
->where('name|title','like','%thinkphp')
```

#### 混合查询 (where 与 whereOr混合使用在复杂场景下)
``` php
$result = Db::table('think_user')->where(function ($query) {
$query->where('id', 1)->whereor('id', 2);
})->whereOr(function ($query) {
$query->where('name', 'like', 'think')->whereOr('name', 'like', 'thinkphp');
})->select();
```

#### getTableInfo 获取表的信息
``` php 
// 获取`think_user`表所有信息
Db::getTableInfo('think_user');
// 获取`think_user`表所有字段
Db::getTableInfo('think_user', 'fields');
// 获取`think_user`表所有字段的类型
Db::getTableInfo('think_user', 'type');
// 获取`think_user`表的主键
Db::getTableInfo('think_user', 'pk');
```
### 查询语法
#### 查询表达式
``` php
where('id','between','1,8');
$map['id'] = array('not between','1,8');
where('id','not in','1,5,8');
where('name','not null');
where('id','exp',' IN (1,3,8) ');
// 正确 推荐写法
$model->whereExp('id', '>score')->find();
```
#### field 

``` php
//可以用于合法性写入
Db::table('think_user')->field('title,email,content')->insert($data);

//在 field中还可以使用函数
Db::table('think_user')->field('id,nickname as name,SUM(score)')->select();
```

#### limit
limit 方法主要用于指定查询和操作的数量，特别是在分页查询的时候。

##### 限制结果数量
```php
->limit(10)
```

##### 分页查询
```php
Db::table('think_article')->limit('10,25')->select();
//或者 ->limit(10,25)
```
表示查找从第10行开始的25条数据

#### page
page 方法是为分页查询而创建的一个人性化操作的方法。

``` php
// 查询第一页数据，page的第一个参数指定页号，比limit更人性
Db::table('think_article')->page('1,10')->select();

```

获取总页数 totalPages

### group

``` php
Db::table('think_user')
->field('user_id,username,max(score)')
->group('user_id')
->select();
```

### having
``` php
Db::table('think_user')
->field('username,max(score)')
->group('user_id')
->having('count(test_time)>3')
->select();
```

### cache
``` php
Db::table('think_user')->cache(true,60)->find();
// 或者使用下面的方式 是等效的
Db::table('think_user')->cache(60)->find();
```

### 时间
``` php
// 获取今天的博客
Db::table('think_blog') ->whereTime('create_time', 'today')->select();
// 获取昨天的博客
Db::table('think_blog')->whereTime('create_time', 'yesterday')->select();
// 获取本周的博客
Db::table('think_blog')->whereTime('create_time', 'week')->select();
// 获取上周的博客

```
### 子查询
1.构造
``` php
$subQuery = Db::table('think_user')
->field('id,name')
->where('id','>',10)
->buildSql();
```

2. 执行
``` php
Db::table($subQuery.' a')
->where('a.name','like','thinkphp')
->order('id','desc')
->select();
```
闭包构造
``` php
Db::table('think_user')
->where('id','IN',function($query){
$query->table('think_profile')->where('status',1)->field('id');
})
->select();

```
### with 连接两个表

``` php
   $list = $this->model
                ->with('taocan,account')
                ->where($where)
                ->order($sort, $order)
                ->paginate($limit);
                
                //model
  public function account()
    {
        return $this->belongsTo("app\admin\model\ShopAccount"[关联表], "shop_account_id"[主表字段], 'id'[关联字段], [], 'LEFT')->setEagerlyType(0);
    }
                
 $data = [
            'total'     => $r->total(),         // 总记录数
            'cur'       => $r->currentPage(),   // 当前页码
            'size'      => $r->listRows(),      // 每页记录数
            'list'      => $r->items()          // 分页数据
        ];
```

## 模型

``` php
$user = new User;
$user->name = 'thinkphp';
$user->email = 'thinkphp@qq.com';
$user->save();
// 获取自增ID
echo $user->id;
```

删除
``` php
// 删除状态为0的数据
User::destroy(['status' => 0]);

```

获取多个数据
``` php
// 使用数组查询
$list = User::all(['status'=>1]);
// 使用闭包查询
$list = User::all(function($query){
$query->where('status', 1)->limit(3)->order('id', 'asc');
});
foreach($list as $key=>$user){
echo $user->name;
}

```
或者在实例化模型后调用查询方法
``` php
$user = new User();
// 查询数据集
$user->where('name', 'thinkphp')
->limit(10)
->order('id', 'desc')
->select();
 ```

## 视图

use think\Controller;
extends Controller

``` php
// 渲染模板输出
return $this->fetch('hello',['name'=>'thinkphp']);
return view('hello',['name'=>'thinkphp']);
```

## 模板
### 请求参数 
``` php
{$Request.get.id}
{$Request.param.name}
```
- 使用函数 {$data.name|md5}
- 默认值 {$Think.get.name|default="名称为空"}
- 运算符 {$user['score']+myFun($user['level'])} //正确的
- 包含文件 {include file="public/header" /} // 包含头部模版header

### 标签
``` php
{volist name="list" id="vo" offset="5" length='10'}
{$vo.name}
{/volist}
```
输出偶数记录
``` php
{volist name="list" id="vo" mod="2" }
{eq name="mod" value="1"}{$vo.name}{/eq}
{/volist}
```
``` php
{for start="开始值" end="结束值" comparison="" step="步进值" name="循环变量名" }
{/for}

```
Case标签还有一个break属性,表示是否需要break,默认是会自动添加break,如果不要break,可以使用:
``` php
{switch name="Think.get.userId|abs"}
{case value="1" break="0"}admin{/case}
{case value="2"}admin{/case}
{default /}default
{/switch}
```

``` php
{between name="Think.post.id" value="1,5"}
输出内容1
{/between}
```

### url
``` html
{:url('aaa/bbb?id='.$vo.id)}
{:url('aaa/bbb',array('id'=>$vo.id))}
{:url('admin/group')}?id={$vo['id']}
```
## 验证

ThinkPHP5.0验证使用独立的\think\Validate类或者验证器进行验证。
### 独立验证
任何时候，都可以使用Validate类进行独立的验证操作，例如：
``` php
$validate = new Validate([
    'name'  => 'require|max:25',
    'email' => 'email'
]);
$data = [
    'name'  => 'thinkphp',
    'email' => 'thinkphp@qq.com'
];
if (!$validate->check($data)) {
    dump($validate->getError());
}
```
这是扩展的方式，继承独立验证的功能，使得控制器内代码更少

``` php
namespace app\index\validate;

use think\Validate;

class User extends Validate
{
    protected $rule = [
        'name'  =>  'require|max:25',
        'email' =>  'email',
    ];

}
```
在需要进行User验证的地方，添加如下代码即可：
``` php
$data = [
    'name'=>'thinkphp',
    'email'=>'thinkphp@qq.com'
];

$validate = Loader::validate('User');

if(!$validate->check($data)){
    dump($validate->getError());
}
```
使用助手函数实例化验证器
``` php
$validate = validate('User');
```

### 设置验证规则
#### session
```php
Session::set('name','thinkphp');
Session::get('name');
```

支持指定 Session 驱动,配置文件如下:
``` php
'session' => [
    'prefix' => 'module',
    'type' => 'redis',
    'auto_start' => true,
    // redis主机
    'host' => '127.0.0.1',
    // redis端口
    'port' => 6379,
    // 密码
    'password' => '',
]
 ```

``` php
// cookie初始化
Cookie::init(['prefix'=>'think_','expire'=>3600,'path'=>'/']);
// 指定当前前缀
Cookie::prefix('think_');

 ```

支持的参数及默认值如下:

``` php
// cookie 名称前缀
'prefix' => '',
// cookie 保存时间
'expire' => 0,
// cookie 保存路径
'path' => '/',
// cookie 有效域名
'domain' => '',
// cookie 启用安全传输
'secure' => false,
// httponly设置
'httponly' => '',
// 是否使用 setcookie
'setcookie' => true,
```

助手函数
系统也提供了助手函数session完成相同的功能，例如：

``` php
// 初始化session
session([
    'prefix'     => 'module',
    'type'       => '',
    'auto_start' => true,
]);

// 赋值（当前作用域）
session('name', 'thinkphp');

// 赋值think作用域
session('name', 'thinkphp', 'think');

// 判断（当前作用域）是否赋值
session('?name');

// 取值（当前作用域）
session('name');

// 取值think作用域
session('name', '', 'think');

// 删除（当前作用域）
session('name', null);

// 清除session（当前作用域）
session(null);

```
#### 多语言

``` php
// 开启语言切换
'lang_switch_on' => true,
```

如果在自动侦测语言的时候,希望设置允许的语言列表,不在列表范围的语言则仍然使用默认语言,可以使用:
``` php
// 设置允许的语言
Lang::setAllowLangList(['zh-cn','en-us']);
```

#### 分页
Thinkphp5 内置了分页对象。

``` php
// 查询状态为1的用户数据 并且每页显示10条数据
$list = Db::name('user')->where('status',1)->paginate(10);
// 把分页数据赋值给模板变量list
$this->assign('list', $list);
// 渲染模板输出
return $this->fetch();
```

返回值的分页对象:
```
[total] => 18
[per_page] => 10
[current_page] => 1
[last_page] => 2
[data] => Array()
```

也可以改成模型的分页查询代码:
``` php
// 查询状态为1的用户数据 并且每页显示10条数据
$list = User::where('status',1)->paginate(10);
// 获取总记录数
$count = $list->total();
// 把分页数据赋值给模板变量list
$this->assign('list', $list);
// 渲染模板输出
return $this->fetch();
```
模板文件中分页输出代码如下:
``` html
<div>
<ul>
{volist name='list' id='user'}
<li> {$user.nickname}</li>
{/volist}
</ul>
</div>
{$list->render()}
```

可以修改样式
``` html
<ul class="pagination">
<li><a href="?page=1">&laquo;</a></li>
<li><a href="?page=1">1</a></li>
<li class="active"><span>2</span></li>
<li class="disabled"><span>&raquo;</span></li>
</ul>
```

分页后数据处理 
``` php
$list = Db::name('user')->where('status',1)->paginate()->each(function($item, $key){$item['nickname'] = 'think'; return $item; });
```

如果要配置分页参数，可以总的配置

| 参数      | 描述        |
| --------- | ----------- |
| list_rows | 每页数量    |
| page      | 当前页      |
| path      | url路径     |
| query     | url额外参数 |
| fragment  | url锚点     |
| var_page  | 分页变量    |
| type      | 分页类名    |

```php
//分页配置
'paginate'               => [
    'type'     => 'bootstrap',
    'var_page' => 'page',
],
```
type属性支持命名空间，例如：
```php
'type'     => '\org\page\bootstrap',
```

也可以在调用分页方法的时候传入，例如：
```php
$list = Db::name('user')->where('status',1)->paginate(10,true,[
    'type'     => 'bootstrap',
    'var_page' => 'page',
    'page' =>3  //指定第几页
]);
```
#### 文件上传

``` html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name="image" /> <br>
<input type="submit" value="上传" />
</form>
```

控制器:
``` php
public function upload(){
// 获取表单上传文件 例如上传了001.jpg
$file = request()->file('image');

// 移动到框架应用根目录/public/uploads/ 目录下
if($file){
$info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 获取扩展名
echo $info->getExtension();
// 输出 20160820/42a79759f284b767dfcb2a0197904287.jpg
echo $info->getSaveName();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}else{
// 上传失败获取错误信息
echo $file->getError();
}
}
```
move 方法成功的话返回的是一个 \think\File 对象,你可以对上传后的文件进行后续操作。


#### 多文件上传

``` html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name="image[]" /> <br>
<input type="file" name="image[]" /> <br>
<input type="file" name="image[]" /> <br>
<input type="submit" value="上传" />
</form>

```

``` php
public function upload(){
// 获取表单上传文件
$files = request()->file('image');
foreach($files as $file){
// 移动到框架应用根目录/public/uploads/ 目录下
$info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}else{
// 上传失败获取错误信息
echo $file->getError();
}
}
}

```

#### 上传验证
``` php
$info = $file->validate(['size'=>15678,'ext'=>'jpg,png,gif'])->move(ROOT_PA
TH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 20160820/42a79759f284b767dfcb2a0197904287.jpg
echo $info->getSaveName();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}
```

#### 上传规则

默认情况下,会在上传目录下面生成以当前日期为子目录,以微秒时间的 md5 编码为文件名的文件,例如上面

生成的文件名可能是:
/home/www/upload/20160510/42a79759f284b767dfcb2a0197904287.jpg

我们可以指定上传文件的命名规则,使用 rule 方法即可,例如:
``` php
// 获取表单上传文件 例如上传了001.jpg
$file = request()->file('image');
// 移动到服务器的上传目录 并且使用md5规则
$file->rule('md5')->move('/home/www/upload/');
```

| 规则 | 描述                        |
|------+-----------------------------|
| date | 根据日期和微秒数生成        |
| md5  | 对文件使用md5_file散列生成  |
| sha1 | 对文件使用sha1_file散列生成 |

rule 后可自定义函数调用

#### 验证码

模版内验证码的显示

``` html
<div>{:captcha_img()}</div>
```

或者

``` html
<div><img src="{:captcha_src()}" alt="captcha" /></div>
```

验证

``` php
$this->validate($data,[
'captcha|验证码'=>'require|captcha'
]);
```
或者手动验证
``` php
if(!captcha_check($captcha)){
//验证失败
};
```

### 图像处理
#### 打开图像
``` php
$image = \think\Image::open('./image.png');
//也可以从直接获取当前请求中的文件上传对象,例如:
$image = \think\Image::open(request()->file('image'));
```

#### 获取图像信息

``` php
$image = \think\Image::open('./image.png');
// 返回图片的宽度
$width = $image->width();
// 返回图片的高度
$height = $image->height();
// 返回图片的类型
$type = $image->type();
// 返回图片的mime类型
$mime = $image->mime();
// 返回图片的尺寸数组 0 图片宽度 1 图片高度
$size = $image->size();
```

#### 裁剪图像
``` php
$image->crop(300, 300)->save('./crop.png');
//支持从某个坐标开始裁剪,例如下面从(100,30)开始裁剪,
$image->crop(300, 300,100,30)->save('./crop.png');
```

``` php
//缩略图
$image->thumb(150, 150)->save('./thumb.png');
// 按照原图的比例生成一个最大为150*150的缩略图并保存为thumb.png
$image->thumb(150,150,\think\Image::THUMB_CENTER)->save('./thumb.png');

//图像翻转
// 对图像进行以y轴进行翻转操作
$image->flip(\think\image::FLIP_Y)->save('./filp_image.png');

//图像旋转
// 对图像使用默认的顺时针旋转90度操作
$image->rotate()->save('./rotate_image.png');

//添加水印
// 给原图左上角添加水印并保存water_image.png，透明度 50%
$image->water('./logo.png',\think\Image::WATER_NORTHWEST,50)->save('water_image.pn
g');
//文字水印
// 给原图左上角添加水印并保存water_image.png
$image->text('十年磨一剑 - 为API开发设计的高性能框架','HYQingKongTiJ.ttf',20,'#ffffff')->save('text_image.png');

```

### 命令行 php think
- clear
- make:controller  index/Blog    [生成index 模块的 Blog 控制器类库文件]
- make:model

### 部署
#### 修改入口文件

``` php
// 应用目录
define('APP_PATH', __DIR__.'/apps/');
// 加载框架引导文件
require './thinkphp/start.php';
```

### sql 日志

第一步：在Database.php文件中将数据库debug设置为true，（默认是true）
``` php
// 数据库调试模式
'debug'           => true,
```
第二步：在Config.php文件中写如下代码

``` php
  'log' => [
        // 日志记录方式，内置 file socket 支持扩展
        'type'  => 'File',
        // 日志保存目录
        'path'  => LOG_PATH,
        // 日志记录级别
        'level' => ['sql'],
    ],
```
一班这样设置之后就可以开启SQL日志记录了。

## 登录方案
### controller\Login.php
``` php
namespace app\admin\controller;
use think\Controller;
use app\admin\model\Login as Log;

class Login extends Controller
{
    public function index()
    {
        // $linkres= \think\Db::name('link')->paginate(3);
        // $this->assign('linkres',$linkres);
        if(request()->isPost()){
            $login=new Log;
            $status=$login->login(input('username'),input('password'));
            if($status==1){
                return $this->success('登录成功，正在跳转！','Index/index');
            }elseif($status==2){
                return $this->error('账号或者密码错误!');
            }else{
                return $this->error('用户不存在!');
            }
        }
        return $this->fetch('login');
    }

    public function logout(){
        session(null);
        return $this->success('退出成功！',url('index'));
    }
}
```

### model\Login.php
``` php
namespace app\admin\model;
use think\Model;
class Login extends Model
{
    public function login($username,$password){
        $admin= \think\Db::name('admin')->where('username','=',$username)->find();
        if($admin){
            if($admin['password']==md5($password)){
                \think\Session::set('id',$admin['id']);
                \think\Session::set('username',$admin['username']);
                return 1;
            }else{
                return 2;
            }
        }else{
            return 3;
        }
    }
}
```
### login.html

