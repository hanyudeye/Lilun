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

将ESC键映射为两次j键                                      

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


vimPlug 插件：https://github.com/junegunn/vim-plug
.vimrc 配置文件
" Vim Plugin
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox' 
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
call plug#end() 

let mapleader = ";"
nnoremap <Leader>q :q<CR>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>g :NERDTreeToggle<CR>
nnoremap <Leader>f :NERDTreeFind<CR>

set clipboard=unnamedplus    " 使用系统剪切版 -> Vim
set clipboard=unnamed      " Vim -> 系统剪切版
colorscheme gruvbox
set nu