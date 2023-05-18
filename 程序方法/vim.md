<<<<<<< HEAD
![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

于 2020-04-10 06:35:25 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

由于疫情原因无法及时返校，需要在家里的windows电脑安装[vim](https://so.csdn.net/so/search?q=vim&spm=1001.2101.3001.7020)并配置环境，在此记录。  
建议使用gvim，而不是在cmd下使用vim。

## 1 下载windows版vim

从github下载windows版的vim：[https://github.com/vim/vim-win32-installer/releases](https://github.com/vim/vim-win32-installer/releases)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020041008264113.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)

## 2 安装vim

1.  双击下载好的gvim\_8.2.0539\_x64.exe文件开始安装，首先选择语言，然后进入欢迎界面，点击next  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410082855204.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
2.  接收协议  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410083646147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
3.  选择要安装的内容，无特殊要求按默认即可，然后点击next  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410083744851.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
4.  选择vim的设置，无特殊要求默认即可，然后点击next  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410083828514.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
5.  选择安装路径  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410084224608.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
6.  安装过程如下，需要等待一会儿  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410084247864.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
7.  显示下面的界面表示安装成功，点击finish结束安装  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410084328355.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)

## 3 添加环境变量

为了能从cmd或者windows terminal直接启动gvim和vim，在环境变量中添加vim的安装路径。

1.  首先在安装路径中找到vim.exe或者gvim.exe（两者在同一文件夹下），复制路径，如下图  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410084856163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
2.  右键此电脑->属性->高级系统设置->环境变量，选中Path，并点击编辑，如下图  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410085211846.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
3.  点击新建，并将刚刚复制的vim.exe所在文件夹的路径粘贴到此处，如下图：  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/2020041008540737.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)
4.  最后点击三个确定（上述过程一共弹出三个窗口，每个窗口一次确定）即添加成功。
5.  添加vim的一个环境变量`$VIM`，右键此电脑->属性->高级系统设置->环境变量，点击上面的新建，如下图  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410190035943.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F5aGFpbGw=,size_16,color_FFFFFF,t_70#pic_center)  
    然后输入新建的环境变量名`VIM`以及变量值，并点击确定  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200410190051618.png#pic_center)

## 3 配置vim

安装好的vim文件夹下有一个`_vimrc`文件，相当于Linux下vim的`.vimrc`文件，在里面配置vim，大多数情况和Linux一样。

配置前准备工作：

-   为了进行颜色主题配置，首先下载solarized主题，从[这里](https://ethanschoonover.com/solarized/)下载后将里面的solarized.vim文件放到安装目录下的vim82文件夹中的colors文件夹下，按笔者的安装路径应该是`C:\Program Files\Vim\vim82\colors`下。
-   在配置某个配置之前，可以先查看一下目前默认的是否开启，如果开启就不用配置了。具体查看方法是，在normal模式下，输入该配置，并加上“？”回车。例如：`:set number?`表示查看是否设置行号。
-   在安装目录下新建`.undo`文件夹（即`C:\Program Files\Vim\.undo`，也可放在自己喜欢的位置)，用来保存历史文件（需要在.vimrc中设置，即下面的配置信息中的`undodir`），使得某个文件关闭后，再次打开也可以还原之前的更改。

1.  基本配置如下

```
" 基本配置
" 
"
" 设置行号
set number
" 语法高亮。自动识别代码，使用多种颜色表示
syntax enable
" 选择颜色主题(已经下载好并放到$VIM/vim82/colors文件夹下) ，推荐自行下载使用solarized主题
colorscheme solarized
" 设置gvim的字体
set guifont=Consolas:h12
" 设置gvim下和外部的复制粘贴
vmap <C-c> "+y
vmap <C-x> "+c
vmap <C-v> c<ESC>"+p
imap <C-v> <C-r><C-o>+
" 支持使用鼠标
set mouse=a
" 按下回车键后，下一行的缩进会自动跟上一行的缩进保持一致
set autoindent
" 按下Tab键后，vim显示的空格数
set tabstop=4
" normal模式下，>>增加一级缩进、<<取消一级缩进、==取消全部缩进时，每一级缩进的空格数
set shiftwidth=4
" 自动将Tab转为空格(防止Tab键在不同编辑器缩进不一致导致问题)
set expandtab
" Tab转为多少个空格
set softtabstop=4
" 光标所在行高亮
set cursorline
highlight CursorLine   cterm=NONE ctermbg=black guibg=NONE guifg=NONE
" 关闭自动折行
set nowrap
" 垂直滚动时，光标距离顶部/底部的距离（单位：行）
set scrolloff=5
" 水平滚动时，光标距离行首或行尾的距离（单位：字符）
set sidescrolloff=30
" 设置行宽，即一行显示多少字符
set textwidth=1000
" 是否显示状态栏：0表示不显示，1表示只在多窗口显示，2表示显示
set laststatus=2
" 设置状态条显示的信息：文件名、光标所在字符的ASCII码、光标所在字符的ASCII码的十六进制、光标所在的位置、光标所在行之上的内容占整个文件的百分比、文件总行数
set statusline=\ %F%m%r%h%w\ \ \ \ ASCII=\%03.3b\ \ \ \ HEX=\%02.2B\ \ \ \ POS=%04l,%04v\ \ \ \ %p%%\ \ \ \ NumOfLine=%L
" 显示行尾的空格
highlight WhitespaceEOL ctermbg=red guibg=red
match WhitespaceEOL /\s\+$/
" 光标遇到括号时，自动高亮对应的另一半括号
set showmatch
" 命令行模式下，在底部显示当前键入的指令。例如键入dd删除一行时，键入第一个d，底部右侧显示d，完全键入dd时，操作完成，底部显示消失
set showcmd
" 搜索时，高亮显示搜索结果
set hlsearch
" 搜索时，每输入一个字符，自动跳到第一个匹配的结果
set incsearch
" 搜索时忽略大小写
set ignorecase
" 不创建交换文件
set noswapfile
" 保留 撤销 操作历史
set undofile
" 设置操作历史文件的保存位置
set undodir=$VIM\.undo
" vim需要记住多少次历史操作
set history=1000
" 命令模式下，底部操作指令按下 Tab 键自动补全。第一次按下 Tab，会显示所有匹配的操作指令的清单；第二次按下 Tab，会依次选择各个指令
set wildmenu
set wildmode=longest:list,full
" 定义F1快捷键为切换vim窗口
map &ltF1&gt &ltC-w&gtw
"设置文件的代码形式 utf8
set encoding=utf-8
set termencoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf-8,chinese,cp936
```

2.  安装vundle插件

-   在安装路径下新建`vimfiles\bundle`文件夹，在cmd执行下面命令：

```
git clone https://github.com/VundleVim/Vundle.vim.git C:\Program Files\Vim\vimfiles\bundle
```

```
如果没有安装git，自行安装后再重新执行上面的命令。
```

3.  在`_vimrc`中添加下面的内容，依次安装各个常用插件，详情参考本人在Linux上配置vim时写的博客：[https://blog.csdn.net/qyhaill/article/details/99701566](https://blog.csdn.net/qyhaill/article/details/99701566)

```
" 插件管理
set rtp+=$VIM\vimfiles\bundle\Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'airblade/vim-gitgutter'
Plugin 'jiangmiao/auto-pairs'
Plugin 'tpope/vim-surround'
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'zxqfl/tabnine-vim'
call vundle#end()
filetype plugin indent on

" 各种插件的配置
"
"
" NERD Commenter配置
" 将leader从"\"改为","
let mapleader = ","
" 在注释符后面自动添加空格
let g:NERDSpaceDelims = 1
" Use compact syntax for prettified multi-line comments：使用紧凑语法美化多行注释
let g:NERDCompactSexyComs = 1
" Align line-wise comment delimiters flush left instead of following code indentation:靠左对齐注释符，而不是跟随代码缩进
let g:NERDDefaultAlign = 'left'
" Allow commenting and inverting empty lines (useful when commenting a region):允许注释和反注释空行（在注释多行代码时很有用）
let g:NERDCommentEmptyLines = 1
" Enable trimming of trailing whitespace when uncommenting:取消注释的同时删除当前行末尾的空格
let g:NERDTrimTrailingWhitespace = 1
" Enable NERDCommenterToggle to check all selected lines is commented or not:暂时不知道什么意思，作什么用途
" let g:NERDToggleCheckAllLines = 1
"
"
" NERDTree配置
" 将F2设置为开关NERDTree的快捷键
map <F2> :NERDTreeToggle<cr>
" 修改树的显示图标
" let g:NERDTreeDirArrowExpandable = '+'
" let g:NERDTreeDirArrowCollapsible = '-'
" 打开vim时如果没有文件自动打开NERDTree
" autocmd vimenter * if !argc()|NERDTree|endif
" 当NERDTree为剩下的唯一窗口时自动关闭
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"
"
" nerdtree-git-plugin配置
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ 'Ignored'   : '☒',
    \ "Unknown"   : "?"
    \ }
```

4.  在cmd打开vim，并执行`:PluginInstall`安装插件。如果遇到提示`:PluginInstall`不是命令的错误，尝试把上面第二行`set rtp +=`后面的内容改为绝对路径。
=======
## VIM
- normal 模式 (控制模式)
- 编辑模式 
- 查找 / 或 ?
- 替换 %s/my/you/g, 表示把文件中所有的my替换成you

- buffer ，tab ,window
- 分割窗口，竖切  :vsp FILE 横切 :sp FILE
- 编辑文件 :e FILE



## 配置 ~/.vimrc

- set nu 设置行号
- syntax on 语法高亮
- colorscheme hybrid 设置主题
- set autoindent 保持上一行的缩进
- set shiftwidth=4 设置缩进单位

## 映射

- (1) 基本映射，在normal模式下

使用map就可以实现映射。比如
```
:nmap <space> viw 就是按下空格选择整个单词
:nmap <c-d> dd 可以使用ctrl+d执行dd删除一行
```

- (2) 在normal/visual/insert模式下都可以定义映射，
使用nmap/vmap/imap定义的映射只在normal/visual/insert分别有效

 - 将ESC键映射为两次j键                                      

```
inoremap jj <Esc>
```
## 插件

### 安装插件管理器 vim-plug


- 安装 [vim-plug](https://github.com/junegunn/vim-plug)

linux
```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

修改 .vimrc 文件

在编辑完.vimrc文件后，我们只需要输入:source ~/.vimrc就可以开始安装插件，再输入:PlugInstall可以查看插件的安装进度


#### 界面美化插件

```
Plug 'vim-airline/vim-airlian'
Plug 'vim-airline/vim-airline-themes'
```

#### 语言插件

- vim-go
- python-mode

#### 其他插件

- 括号，引号成对编辑的插件 vim-surround 插件
- 快速浏览代码插件 vim-tagbar
- 文件格式化的插件 lbdchd/neoformat
>>>>>>> 5f96f5542f022ff52bca98512f3aa7d48260c2b8
