
## 打开 vscode 软件

- 方法1 
<!-- 我测试 已失效 -->
1. 打开命令面板,command+shift+p
2. 输入Shell Command；
3. 此时会有提示“Shell Command: Install ‘code’ command in PATH”，运行即可；
4. 关闭vscode，直接在终端中输入code .，则打开vscode。

- 方法2
直接使用命令 code.cmd 打开

## vscode 折叠

## 插件 
### settings Sync
- 通过GitHub生成你的gist Id 和 token
- 两台电脑的VSCode中都需要安装settings Sync插件并配置 gistId 和 token
- 原电脑上传配置
- 新电脑下载同步配置


### 搜索 search

### epub reader

由于vscode安全策略，书架编辑请在插件安装目录 win:[C:\Users\ 你的用户名.vscode\extensions\renkun.reader\book],mac:[~/.vscode/extensions/renkun.reader/book]

AD 翻页

### 隐藏滚动条

文本编辑器->所有语言-> 滚动条

### 设置本地变量
1. 创建配置文件  .vscode/settings.json
2. 添加内容

```json
{
    "pasteImage.path": "${currentFileDir}/asserts/images/"
}
```

### vscode 代码运行 中文