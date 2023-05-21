## 什么是 git?

 文件历史记录
- 存储新历史 (历史中切换)


## 分支操作
1、git branch 创建分支
假如有个开发版一直在开发，到有个稳定时刻，创建一个稳定版，继续开发，再有稳定的就再创建。


2、git branch -b 创建并切换到新建的分支上

3、git checkout 切换分支

4、git branch 查看分支列表

5、git branch -v 查看所有分支的最后一次操作

6、git branch -vv 查看当前分支

7、git brabch -b 分支名 origin/分支名 创建远程分支到本地

8、git branch --merged 查看别的分支和当前分支合并过的分支

9、git branch --no-merged 查看未与当前分支合并的分支

10、git branch -d 分支名 删除本地分支

11、git branch -D 分支名 强行删除分支

12、git branch origin :分支名 删除远处仓库分支

13、git merge 分支名 合并分支到当前分支上

## 暂存操作
1、git stash 暂存当前修改

2、git stash apply 恢复最近的一次暂存

3、git stash pop 恢复暂存并删除暂存记录

4、git stash list 查看暂存列表

5、git stash drop 暂存名(例：stash@{0}) 移除某次暂存

6、git stash clear 清除暂存

## 回退操作
1、git reset --hard HEAD^ 回退到上一个版本

2、git reset --hard ahdhs1(commit_id) 回退到某个版本

3、git checkout -- file撤销修改的文件(如果文件加入到了暂存区，则回退到暂存区的，如果文件加入到了版本库，则还原至加入版本库之后的状态)

4、git reset HEAD file 撤回暂存区的文件修改到工作区

## 标签操作

1、git tag 标签名 添加标签(默认对当前版本)

2、git tag 标签名 commit_id 对某一提交记录打标签

3、git tag -a 标签名 -m '描述' 创建新标签并增加备注

4、git tag 列出所有标签列表

5、git show 标签名 查看标签信息

6、git tag -d 标签名 删除本地标签

7、git push origin 标签名 推送标签到远程仓库

8、git push origin --tags 推送所有标签到远程仓库

9、git push origin :refs/tags/标签名 从远程仓库中删除标签

## 其它操作

### 常规操作

1、git push origin test 推送本地分支到远程仓库

2、git rm -r --cached 文件/文件夹名字 取消文件被版本控制

3、git reflog 获取执行过的命令

4、git log --graph 查看分支合并图

5、git merge --no-ff -m '合并描述' 分支名 不使用Fast forward方式合并，采用这种方式合并可以看到合并记录

6、git check-ignore -v 文件名 查看忽略规则

7、git add -f 文件名 强制将文件提交

### git创建项目仓库

1、git init 初始化
2、git remote add origin url 关联远程仓库
3、git pull
4、git fetch 获取远程仓库中所有的分支到本地

### 忽略已加入到版本库中的文件

1、git update-index --assume-unchanged file 忽略单个文件
2、git rm -r --cached 文件/文件夹名字 (. 忽略全部文件)

### 取消忽略文件

git update-index --no-assume-unchanged file

### 拉取、上传免密码

git config --global credential.helper store

## 初始化配置

```
git config --global user.email XX
git config --global user.name XX
```
## 创建 ssh key

ssh-keygen -t rsa -C XX 

测试  ssh-v git@github.com

## 中文文件名乱码
git 默认中文文件名是 \xxx\xxx 等八进制形式，是因为 对0x80以上的字符进行quote。

只需要设置core.quotepath设为false，就不会对0x80以上的字符进行quote。中文显示正常

git config --global core.quotepath false

## WSL 使用中遇到 换行符 的问题及解决方案 

 > Git 仓库中所有文件被标记为 modified


换行符转换设置为 input，即提交时把 CRLF 转换成 LF，检出时不转换。
```
git config --global core.autocrlf input
```

## question
### git 取消对文件的跟踪
git rm 
### git 排除入库的文件
对于已入库的文件，取消状态跟踪
命令：git update-index –assume-unchanged FILENAME 路径+文件名

# github
- 趋势 https://github.com/trending

## 一些问题
### fatal: protocol 'https' is not supported
当你使用 Ctrl +v 在终端粘贴的时候，不会成功，但会粘贴一个隐藏的符号 ^? ， 删除掉就可以了。

## 代码仓库  github

- [热门](https://github.com/trending)
- [专题](https://github.com/topics)

搜索
``` 
优秀项目  Awesome + 关键字  
stars: fork
qt in:name：表示在项目名称中搜索 qt 关键字
qt in:readme：表示在项目 readme 中搜索 qt 关键字
qt in:description：表示在 项目描述中搜索 qt 关键字
qt in:USERNAME：表示在 USERNAME 中搜索 qt 关键字
qt in:ORGNAME：表示在组织或机构名中搜索 qt 关键字
size:>=5000 Qt ：搜索大小超过 5M 的包含 Qt 关键字项目
language:C++ location:china 搜索国内的开发者，语言限定为 C++
``` 
后缀
```
stars:>20 extension:el language:elisp
```

