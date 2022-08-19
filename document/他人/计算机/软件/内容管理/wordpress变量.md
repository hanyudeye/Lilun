获取和使用 WordPress 中的全局变量
 2019-01-02
 2,359
和其他 PHP 系统一样，WordPress 会定义一些全局变量来方便数据的访问，基本上 WordPress 生成的所有数据都可以在全局变量中找到，了解 WordPress 中有哪些全局变量，可以方便我们了解 WordPress 的数据，从而更加深入的了解 WordPress ，为 WordPress主题开发打下更加坚实的基础。

WordPress 中默认的全局变量
在循环中可以使用的全局变量
在 WordPress 循环中，全局变量已经被提前获取到了，我们可以直接使用。这些全局变量包含了循环中当前文章的信息。

$post (WP_Post) 当前文章对象
$authordata (WP_User) 当前文章作者对象
$currentday (string) 当前文章的发布日期
$currentmonth (string) 当前文章的发布月份
$page (int) 当前文章被访问的分页，通过查询参数 page 定义
$pages (array) 当前文章的分页信息，每个分页元素包含了 <!--nextpage--> 标签分隔的部分
$multipage (boolean) 当前文章是否为多页文章，根据上面的 $pages 参数检测
$more (boolean) WordPress 是否执行 <!--more--> 标签的标记，如果为 true，WordPress 将不会执行 more 标签
$numpages (int) 返回当前文章的总页数，和上面的 $pages x相关
检测浏览器的布尔值
下面的全局变量存储着关于用户浏览器的检测信息，值为布尔值，可以用来用户用来访问网站的浏览器。

$is_iphone (boolean) iPhone Safari
$is_chrome (boolean) Google Chrome
$is_safari (boolean) Safari
$is_NS4 (boolean) Netscape 4
$is_opera (boolean) Opera
$is_macIE (boolean) Mac Internet Explorer
$is_winIE (boolean) Windows Internet Explorer
$is_gecko (boolean) FireFox
$is_lynx (boolean)
$is_IE (boolean) Internet Explorer
$is_edge (boolean) Microsoft Edge
检测网站服务器的布尔值
下面的全局变量存储着关于网站服务器的一些信息，可以用来判断运行网站的服务器类型。

$is_apache (boolean) Apache HTTP Server
$is_IIS (boolean) Microsoft Internet Information Services (IIS)
$is_iis7 (boolean) Microsoft Internet Information Services (IIS) v7.x
$is_nginx (boolean) Nginx web server
版本变量
下面的变量存储着 WordPress 中的一些版本信息。

$wp_version (string) 当前安装的 WordPress 版本
$wp_db_version (int) 当前数据库的版本
$tinymce_version (string) TinyMCE 的版本
$manifest_version (string) 缓存 manifest 的版本
$required_php_version (string) 网站安装的 WordPress 版本需要的最小 PHP 版本
$required_mysql_version (string) 网站安装的 WordPress 需要的最小 MySQL 版本
其他全局变量
$super_admins (array) 拥有超级管理员权限的用户 ID, 此全局变量只对站点所有者注册
$wp_query (object) Class_Reference/WP_Query 类实例
$wp_rewrite (object) Class_Reference/WP_Rewrite 类实例
$wp (object) Class_Reference/WP 类实例
$wpdb (object) Class_Reference/wpdb 类实例
$wp_locale (object)  本地化信息
$wp_admin_bar (WP_Admin_Bar)  管理工具条对象
$wp_roles (WP_Roles) WordPress 角色对象
$wp_meta_boxes (array) 已注册 metaboxes 的对象, 包含他们的 id, 参数, 回调函数、标题等信息
$wp_registered_sidebars (array) 已注册的小工具区域
$wp_registered_widgets (array) 已注册的小工具
$wp_registered_widget_controls (array) 已注册的小工具字段
$wp_registered_widget_updates (array) 已注册的小工具更新
后台全局变量
$pagenow (string) 在 wp-admin 中使用，同时参考 get_current_screen() 以了解 WordPress Admin Screen API
$post_type (string) 在 wp-admin 中使用，当前页面的文章类型
$allowedposttags (array) 允许使用的文章标签
$allowedtags (array) 允许使用的标签
$menu (array) WordPress 的后台菜单数据
访问 WordPress 中的全局变量
我们可以通过下面的方式直接获取全局变量来使用，WordPress 的每个全局变量也都可以通过对应的函数来获取，WordPress 官方推荐的方式是用过函数的方式来获取这些全局变量。

global $wp_version;
// 或者
$wp_version = get_bloginfo('version');
echo $wp_version;
获取 WordPress 中的全局变量
除了 WordPress 内核注册的全局变量，一些主题和插件也有可能会注册一些全局变量，如果需要查看系统中已经注册的所有全局变量，可以通过下面的代码查看。

echo "<pre>";
print_r($GLOBALS);
echo "</pre>";