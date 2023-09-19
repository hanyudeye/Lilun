## Github Action 快速上手指南

## Github Action 是什么？

用人话说，**就是你可以给你的代码仓库部署一系列自动化脚本，在你进行了提交/合并分支等操作后，自动执行脚本。**

GitHub Actions 有一些自己的术语：

-   workflow （工作流程）：持续集成一次运行的过程，就是一个 workflow。
-   job （任务）：一个 workflow 由一个或多个 jobs 构成，含义是一次持续集成的运行，可以完成多个任务。
-   step（步骤）：每个 job 由多个 step 构成，一步步完成。
-   action （动作）：每个 step 可以依次执行一个或多个命令（action）。

看这些介绍和定义，其实比较枯燥，我们直接来看代码实现，在代码中来理解这些定义和指令。

## 快速上手

## 给仓库创建新文件夹.github/workflow

首先，用你自己的任意GitHub仓库，在仓库内添加文件夹`.github/workflow` 或者`.github/workflows`：


> 一个库可以有多个 workflow 文件。GitHub 只要发现.github/workflows目录里面有.yml文件，就会自动运行该文件。

## 撰写你的workflow

一个yml脚本便是Action的核心了，我们新建一个`blank.yml`，内容如下：

![](https://upload-images.jianshu.io/upload_images/5718317-b3a6f51ab3bd7602.png?imageMogr2/auto-orient/strip|imageView2/2/w/1054/format/webp)

image

我在代码里做了一些注释，帮助大家理解每个指令的含义。

整个脚本大致的流程如下：

-   指定在push或者pull request时触发脚本执行
-   拉取ubuntu最新版的镜像
-   缓存Maven依赖目录，避免每次都下载全量依赖包，加快执行速度
-   安装Java8
-   指定pom.xml文件路径，随后用Maven编译项目
-   运行Junit单元测试

## 给项目撰写单元测试代码

ok，写完脚本，我们需要来编写一些测试代码，让Junit有事可做。

我使用了自己的一个仓库，上面有完整的action脚本和测试类代码，供参考：

[https://github.com/qqxx6661/awesome-utils](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqqxx6661%2Fawesome-utils)

这是一个Maven仓库，我们在test文件夹内加入测试代码。

![](https://upload-images.jianshu.io/upload_images/5718317-9e6894168c287546.png?imageMogr2/auto-orient/strip|imageView2/2/w/685/format/webp)

image

上面的测试代码测试的是下面的一个静态方法：

![](https://upload-images.jianshu.io/upload_images/5718317-15c9e463192cb8e7.png?imageMogr2/auto-orient/strip|imageView2/2/w/656/format/webp)

image

## 提交代码，触发Github Action执行

将代码commit并push后，点开你的仓库主页，点击Action标签：

![](https://upload-images.jianshu.io/upload_images/5718317-3717d60bd8e54574.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image

可以看到已经有了执行信息。

接着看下我们的Action到底有没有执行，点开Action标签，已经发现了Junit：

![](https://upload-images.jianshu.io/upload_images/5718317-529fd0c9372eae2b.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image

可以进行脚本代码的在线编辑：

![](https://upload-images.jianshu.io/upload_images/5718317-33b5e8b976cd53e9.png)

image

点进本次commit执行的记录，可以看到，action顺利完成了几个步骤：

![](https://upload-images.jianshu.io/upload_images/5718317-fb17792bd71a759f.png)

image

点开Maven的构建日志，可以看到我们第一次跑action，所有的依赖还是即时下载的：

![](https://upload-images.jianshu.io/upload_images/5718317-483c09048a054790.png)

image

单元测试运行的日志输出正常：

![](https://upload-images.jianshu.io/upload_images/5718317-3b3c16fb07e5e9c3.png)

image

为了试验Maven的依赖包是否能够使用到缓存，我们再写几个单元测试，然后commit：

![](https://upload-images.jianshu.io/upload_images/5718317-4c2f720adf147428.png)

image

可以看到，新的action日志里直接开始了编译，不再需要下载全量的包：

![](https://upload-images.jianshu.io/upload_images/5718317-b043514b97bbcd83.png)

image

单元测试页成功执行：

![](https://upload-images.jianshu.io/upload_images/5718317-b7113af71921f688.png)

image

至此，我们的简易入门教程便结束了。

## 还有很多功能等待探索

当然，这还只是Action的冰山一角，其能做的事情远不止于此：

-   编译打包代码
-   自动上传至公有云/App容器
-   单元测试/代码覆盖率测试/文档同步/发布版本

等着你们的探索。

![](https://upload-images.jianshu.io/upload_images/5718317-63de237cc8af419d.png)

image

## 参考

[https://docs.github.com/cn/actions/guides/building-and-testing-python#publishing-to-package-registries](https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.github.com%2Fcn%2Factions%2Fguides%2Fbuilding-and-testing-python%23publishing-to-package-registries)

[http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html](https://links.jianshu.com/go?to=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2019%2F09%2Fgetting-started-with-github-actions.html)

**如果文章对你有帮助，求各位大佬点赞支持一下，你的点赞和在看是我更新的动力~**

更多精彩内容，就在简书APP

![](https://upload.jianshu.io/images/js-qrc.png)

"如果文章对你有帮助，不妨收藏，投食，转发，在看起来~"

还没有人赞赏，支持一下

[![  ](https://upload.jianshu.io/users/upload_avatars/5718317/f30221ef-e592-4e44-a04d-a7fcf5bd9431.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp)](https://www.jianshu.com/u/b5f225ca2376)

[蛮三刀酱](https://www.jianshu.com/u/b5f225ca2376 "蛮三刀酱")公众号：后端技术漫谈/蛮三刀酱<br><br>同步更新各大博客

总资产19共写了33.1W字获得270个赞共298个粉丝

-   序言：七十年代末，一起剥皮案震惊了整个滨河市，随后出现的几起案子，更是在滨河造成了极大的恐慌，老刑警刘岩，带你破解...
    
-   序言：滨河连续发生了三起死亡事件，死亡现场离奇诡异，居然都是意外死亡，警方通过查阅死者的电脑和手机，发现死者居然都...
    
-   文/潘晓璐 我一进店门，熙熙楼的掌柜王于贵愁眉苦脸地迎上来，“玉大人，你说我怎么就摊上这事。” “怎么了？”我有些...
    
-   文/不坏的土叔 我叫张陵，是天一观的道长。 经常有香客问我，道长，这世上最难降的妖魔是什么？ 我笑而不...
    
-   正文 为了忘掉前任，我火速办了婚礼，结果婚礼上，老公的妹妹穿的比我还像新娘。我一直安慰自己，他们只是感情好，可当我...
    
    [![](https://upload.jianshu.io/users/upload_avatars/4790772/388e473c-fe2f-40e0-9301-e357ae8f1b41.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)茶点故事](https://www.jianshu.com/u/0f438ff0a55f)阅读 15,215评论 0赞 116
    
-   文/花漫 我一把揭开白布。 她就那样静静地躺着，像睡着了一般。 火红的嫁衣衬着肌肤如雪。 梳的纹丝不乱的头发上，一...
    
-   那天，我揣着相机与录音，去河边找鬼。 笑死，一个胖子当着我的面吹牛，可吹牛的内容都是我干的。 我是一名探鬼主播，决...
    
-   文/苍兰香墨 我猛地睁开眼，长吁一口气：“原来是场噩梦啊……” “哼！你这毒妇竟也来了？” 一声冷哼从身侧响起，我...
    
-   想象着我的养父在大火中拼命挣扎，窒息，最后皮肤化为焦炭。我心中就已经是抑制不住地欢快，这就叫做以其人之道，还治其人...
    
-   序言：老挝万荣一对情侣失踪，失踪者是张志新（化名）和其女友刘颖，没想到半个月后，有当地人在树林里发现了一具尸体，经...
    
-   正文 独居荒郊野岭守林人离奇死亡，尸身上长有42处带血的脓包…… 初始之章·张勋 以下内容为张勋视角 年9月15日...
    
    [![](https://upload.jianshu.io/users/upload_avatars/4790772/388e473c-fe2f-40e0-9301-e357ae8f1b41.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)茶点故事](https://www.jianshu.com/u/0f438ff0a55f)阅读 6,441评论 1赞 105
    
-   正文 我和宋清朗相恋三年，在试婚纱的时候发现自己被绿了。 大学时的朋友给我发了我未婚夫和他白月光在一起吃饭的照片。...
    
    [![](https://upload.jianshu.io/users/upload_avatars/4790772/388e473c-fe2f-40e0-9301-e357ae8f1b41.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)茶点故事](https://www.jianshu.com/u/0f438ff0a55f)阅读 7,006评论 0赞 101
    
-   白月光回国，霸总把我这个替身辞退。还一脸阴沉的警告我。\[不要出现在思思面前， 不然我有一百种方法让你生不如死。\]我...
    
-   序言：一个原本活蹦乱跳的男人离奇死亡，死状恐怖，灵堂内的尸体忽然破棺而出，到底是诈尸还是另有隐情，我是刑警宁泽，带...
    
-   正文 年R本政府宣布，位于F岛的核电站，受9级特大地震影响，放射性物质发生泄漏。R本人自食恶果不足惜，却给世界环境...
    
    [![](https://upload.jianshu.io/users/upload_avatars/4790772/388e473c-fe2f-40e0-9301-e357ae8f1b41.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)茶点故事](https://www.jianshu.com/u/0f438ff0a55f)阅读 7,328评论 3赞 102
    
-   文/蒙蒙 一、第九天 我趴在偏房一处隐蔽的房顶上张望。 院中可真热闹，春花似锦、人声如沸。这庄子的主人今日做“春日...
    
-   文/苍兰香墨 我抬头看了看天上的太阳。三九已至，却和暖如春，着一层夹袄步出监牢的瞬间，已是汗流浃背。 一阵脚步声响...
    
-   我被黑心中介骗来泰国打工， 没想到刚下飞机就差点儿被人妖公主榨干…… 1. 我叫王不留，地道东北人。 一个月前我还...
    
-   正文 我出身青楼，却偏偏与公主长得像，于是被迫代替她去往敌国和亲。 传闻我的和亲对象是个残疾皇子，可洞房花烛夜当晚...
    
    [![](https://upload.jianshu.io/users/upload_avatars/4790772/388e473c-fe2f-40e0-9301-e357ae8f1b41.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)茶点故事](https://www.jianshu.com/u/0f438ff0a55f)阅读 8,617评论 1赞 110
    

### 被以下专题收入，发现更多相似内容

### 推荐阅读[更多精彩内容](https://www.jianshu.com/)

-   概念 GitHub Actions\[https://github.com/features/actions\] 是 ...
    
-   体验分享 本文一个尝鲜的体验分享, 并没有太复杂的技巧, 做了一个最少代码的例子展示, 让每个人都可以把actio...
    
    [![](https://upload.jianshu.io/users/upload_avatars/12342531/3851b09a-98bd-4b98-953d-7b140b96fbab?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)铁皮饭盒](https://www.jianshu.com/u/9e19f50fb0eb)阅读 1,483评论 0赞 50
    
-   Spark 编程指南 概述 Spark 依赖 初始化 Spark 使用 Shell 弹性分布式数据集 (RDDs)...
    
-   今天的越写悦快乐之系列文章为大家带来Vue项目如何使用GitHub Actions进行自动发布。众所周知，GitH...
    
-   Spark 编程指南 概述 Spark 依赖 初始化 Spark 使用 Shell 弹性分布式数据集 (RDDs)...
    
    [![](https://upload.jianshu.io/users/upload_avatars/2923610/4ebe67ff-1e3e-4b22-8b4c-518d66eaccf7.JPG?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48/format/webp)草里有只羊](https://www.jianshu.com/u/a5d135d71592)阅读 3,123评论 0赞 15