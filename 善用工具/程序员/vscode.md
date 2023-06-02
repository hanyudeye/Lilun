# VSCode

## 用户自定义配置文件settings.json

## 默认配置defaultSettings.json

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

### 扩展

- 简体中文
- Live Server
- Code Runner
- px to rem
- vue language features(volar)
- vue vscode snippets
- Code Spell Checker
=======
### Vue 扩展  vue language features

### Auto Close Tag 自动闭合标签
输入标签名称的时候自动生成闭合标签

### Auto Rename Tag 尾部闭合标签同步修改
自动检测配对标签，同步修改

### Vscode-element-helper 

提示 element 标签名称

### element-ui-helper 组件属性提示
### live server 热更新插件

### Browser Preview 直接预览插件
VSCode 常用操作和配置
===

> create by **jsliang** on **2018-09-04 11:26:11**  
> Recently revised in **2019-05-30 19:22:28**

## 第一节 VSCode配置

配置方式： 主菜单 -> 文件 -> 首选项 -> 用户设置：

```
{
    "editor.wordSeparators": "./\\()\"':,.;<>~!@#$%^&*|+=[]{}`~?",
    "git.autofetch": true,
    "markdown.styles": [
        "E:\\MyWeb\\jsliang-study\\Document-Library\\public-repertory\\css\\markdown-github.css"
    ],
    "file.exclude": {
        "node_modules/": true
    }
}
```

### 1.1 下划线选中

设置不仅可以下划线选中，而且可以横杠选中，主要应用于同事写 class 名或者 id 名或者写 js 起名的时候，有可能用 - 或者 _ 。

```
{
    "editor.wordSeparators": "./\\()\"':,.;<>~!@#$%^&*|+=[]{}`~?"
}
```

### 1.2 监听 git fetch

git fetch 命令用于从另一个存储库下载对象和引用，在 vs code 中配置 git.fetch 功能，从而启动自动提取。`当然一般不会有问题，但是在环境中使用tar压缩源码时，vs code后台会来 git fetch 导致压缩失败，可以视情况关闭`

```
{
    "git.autofetch": true,
}
```

### 1.3 配置 Markdown 预览的样式

如果是VS Code默认的配置，Markdown 文件是乌漆嘛黑的，这时候可以给它设置个 GitHub 样式，这样子预览看到的就是 GitHub 中的样式，详情可看：[点击跳往](../markdown/markdown.md)

```
{
    "markdown.styles": [
        "E:\\MyWeb\\jsliang-study\\Document-Library\\public-repertory\\css\\markdown-github.css"
    ],
}
```

### 1.4 忽略 node_modules 文件夹

设置这个，vs code 就不会理会 node_modules 文件夹了。详情可看：[点击跳往](../git/git.md)

```
{
    "file.exclude": {
        "node_modules/": true
    }
}
```

### 1.5 VS Code 设置模板页

1. 安装插件 HTML Snippets
2. 文件-首选项-用户代码片段-HTML
3. 修改文件内容为：
```
{
  // Place your snippets for html here. Each snippet is defined under a snippet name and has a prefix, body and 
  // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
  // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
  // same ids are connected.
  // Example:
  // "Print to console": {
  //  "prefix": "log",
  //  "body": [
  //      "console.log('$1');",
  //      "$2"
  //  ],
  //  "description": "Log output to console"
  // }
  "!!": {
  "prefix": "!!",
  "body": [
    "<!DOCTYPE html>",
    "<html lang=\"en\">",
    "<head>",
    "\t<meta charset=\"UTF-8\">",
    "\t<meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no\">",
    "\t<meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">",
    "\t<title>HelloWorld</title>",
    "</head>",
    "<body>",
    "\t$1",
    "\t",
    "\t<script src=\"https://cdn.bootcss.com/jquery/3.3.1/jquery.js\"></script>",
    "</body>",
    "</html>"
  ],
  "description": "!! - Defines a template for a html5 document"
  }
}
```
4. 在HTML页面输入!!然后回车，即可看到新效果

## 第二节 插件推荐

* Prettier - Code formatter：格式化代码
* Vetur - 管理好你的 Vue 代码

## 自动换行

点击菜单栏 View--> Toggle Word Wrap 选项

或者直接 快捷键 : alt + Z

MacOS 快捷键：option + Z

## 当前配置

{
    "vim.easymotion": true,
    "vim.useSystemClipboard": true,
    "vim.insertModeKeyBindings": [
        {
            "before": [
                "k",
                "j"
            ],
            "after": [
                "<Esc>"
            ]
        }
    ],
    "vim.normalModeKeyBindingsNonRecursive": [
        {
            "before": [
                "<space>"
            ],
            "commands": [
                "vspacecode.space"
            ]
        },
        {
            "before": [
                ","
            ],
            "commands": [
                "vspacecode.space",
                {
                    "command": "whichkey.triggerKey",
                    "args": "m"
                }
            ]
        }
    ],
    "vim.visualModeKeyBindingsNonRecursive": [
        {
            "before": [
                "<space>"
            ],
            "commands": [
                "vspacecode.space"
            ]
        },
        {
            "before": [
                ","
            ],
            "commands": [
                "vspacecode.space",
                {
                    "command": "whichkey.triggerKey",
                    "args": "m"
                }
            ]
        }
    ],
    "security.workspace.trust.untrustedFiles": "open",
    "sync.gist": "3315a2db0f6382dc94e5a2ec3fc41c29",
    "sync.autoUpload": true,
    "sync.autoDownload": true,
    "sync.quietSync": true,
    "files.associations": {
        "*.cjson": "jsonc",
        "*.wxss": "css",
        "*.wxs": "javascript"
    },
    "emmet.includeLanguages": {
        "wxml": "html"
    },
    "minapp-vscode.disableAutoConfig": true,
    "workbench.startupEditor": "none",
    "editor.minimap.enabled": false,
    "editor.fontFamily": "monospace,Consolas, 'Courier New', ",
    "explorer.confirmDelete": false,
    "code-runner.runInTerminal": true,
    "redhat.telemetry.enabled": true,
    //终端颜色配置
    "workbench.colorCustomizations": {
        //可以将鼠标放到下面的色号上根据自己的偏好进行选择
        "terminal.foreground": "#37FF13",
        "terminal.background": "#2b2424"
    },
    "terminal.integrated.cursorBlinking": true,
    "terminal.integrated.lineHeight": 1.2,
    "terminal.integrated.letterSpacing": 0.1,
    "terminal.integrated.fontSize": 15, //字体大小设置
    "terminal.integrated.fontFamily": "Lucida Console",
    "window.title": "${folderName}",
    "explorer.confirmDragAndDrop": false,
    "[php]": {
        "editor.defaultFormatter": "bmewburn.vscode-intelephense-client"
    },
    "editor.lineNumbers": "off",
    "pasteImage.path": "${currentFileDir}/images/",
    // "workbench.colorTheme": "Monokai",
    "liveServer.settings.donotVerifyTags": true,
    "liveServer.settings.donotShowInfoMsg": true,
    "git.confirmSync": false,
    "editor.unicodeHighlight.invisibleCharacters": false,
    "git.enableSmartCommit": true,
    "magit.display-buffer-function": "same-column",
    "workbench.colorTheme": "Visual Studio Dark",
    "google-translate.serverDomain": "https://translate.amz.wang",
    // "git.confirmSync": false, //字体设置
}

# 之前

{
    "editor.lineNumbers": "off",
    "editor.minimap.enabled": false,
    "vim.useCtrlKeys": true,
    "vim.useSystemClipboard": true,
    "vim.insertModeKeyBindings": [
        {
            "before": [
                "k",
                "j"
            ],
            "after": [
                "<Esc>"
            ]
        },
        {
            "key": "alt+l",
            "command": "cursorRight",
            "when": "editorTextFocus"
        },
        {
            "key": "alt+h",
            "command": "cursorLeft",
            "when": "editorTextFocus"
        },
        {
            "key": "space",
            "command": "vspacecode.space",
            "when": "activeEditorGroupEmpty && focusedView == '' && !whichkeyActive && !inQuickOpen"
        },
        {
            "key": "tab",
            "command": "extension.vim_tab",
            "when": "editorFocus && vim.active && !inDebugRepl && vim.mode != 'Insert' && editorLangId != 'magit'"
        },
        {
            "key": "tab",
            "command": "-extension.vim_tab",
            "when": "editorFocus && vim.active && !inDebugRepl && vim.mode != 'Insert'"
        },
        {
            "key": "x",
            "command": "magit.discard-at-point",
            "when": "editorTextFocus && editorLangId == 'magit' && vim.mode =~ /^(?!SearchInProgressMode|CommandlineInProgress).*$/"
        },
        {
            "key": "k",
            "command": "-magit.discard-at-point"
        },
        {
            "key": "-",
            "command": "magit.reverse-at-point",
            "when": "editorTextFocus && editorLangId == 'magit' && vim.mode =~ /^(?!SearchInProgressMode|CommandlineInProgress).*$/"
        },
        {
            "key": "v",
            "command": "-magit.reverse-at-point"
        },
        {
            "key": "shift+-",
            "command": "magit.reverting",
            "when": "editorTextFocus && editorLangId == 'magit' && vim.mode =~ /^(?!SearchInProgressMode|CommandlineInProgress).*$/"
        },
        {
            "key": "shift+v",
            "command": "-magit.reverting"
        },
        {
            "key": "shift+o",
            "command": "magit.resetting",
            "when": "editorTextFocus && editorLangId == 'magit' && vim.mode =~ /^(?!SearchInProgressMode|CommandlineInProgress).*$/"
        },
        {
            "key": "shift+x",
            "command": "-magit.resetting"
        },
        {
            "key": "x",
            "command": "-magit.reset-mixed"
        },
        {
            "key": "ctrl+u x",
            "command": "-magit.reset-hard"
        },
        {
            "key": "y",
            "command": "-magit.show-refs"
        },
        {
            "key": "y",
            "command": "vspacecode.showMagitRefMenu",
            "when": "editorTextFocus && editorLangId == 'magit' && vim.mode == 'Normal'"
        },
        {
            "key": "ctrl+j",
            "command": "workbench.action.quickOpenSelectNext",
            "when": "inQuickOpen"
        },
        {
            "key": "ctrl+k",
            "command": "workbench.action.quickOpenSelectPrevious",
            "when": "inQuickOpen"
        },
        {
            "key": "ctrl+j",
            "command": "selectNextSuggestion",
            "when": "suggestWidgetMultipleSuggestions && suggestWidgetVisible && textInputFocus"
        },
        {
            "key": "ctrl+k",
            "command": "selectPrevSuggestion",
            "when": "suggestWidgetMultipleSuggestions && suggestWidgetVisible && textInputFocus"
        },
        {
            "key": "ctrl+l",
            "command": "acceptSelectedSuggestion",
            "when": "suggestWidgetMultipleSuggestions && suggestWidgetVisible && textInputFocus"
        },
        {
            "key": "ctrl+j",
            "command": "showNextParameterHint",
            "when": "editorFocus && parameterHintsMultipleSignatures && parameterHintsVisible"
        },
        {
            "key": "ctrl+k",
            "command": "showPrevParameterHint",
            "when": "editorFocus && parameterHintsMultipleSignatures && parameterHintsVisible"
        },
        {
            "key": "ctrl+h",
            "command": "file-browser.stepOut",
            "when": "inFileBrowser"
        },
        {
            "key": "ctrl+l",
            "command": "file-browser.stepIn",
            "when": "inFileBrowser"
        },
        {
            "key": "ctrl+alt+b",
            "command": "workbench.action.toggleActivityBarVisibility"
        }
    ],
    "vim.normalModeKeyBindingsNonRecursive": [
        {
            "before": [
                "<space>"
            ],
            "commands": [
                "vspacecode.space"
            ]
        },
        {
            "before": [
                ","
            ],
            "commands": [
                "vspacecode.space",
                {
                    "command": "whichkey.triggerKey",
                    "args": "m"
                }
            ]
        }
    ],
    "vim.visualModeKeyBindingsNonRecursive": [
        {
            "before": [
                "<space>"
            ],
            "commands": [
                "vspacecode.space"
            ]
        },
        {
            "before": [
                ","
            ],
            "commands": [
                "vspacecode.space",
                {
                    "command": "whichkey.triggerKey",
                    "args": "m"
                }
            ]
        }
    ],
    "sync.gist": "3315a2db0f6382dc94e5a2ec3fc41c29",
    "sync.autoUpload": false,
    "sync.autoDownload": false,
    "sync.quietSync": false,
    "workbench.startupEditor": "newUntitledFile",
    "[jsonc]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
    "liveServer.settings.donotShowInfoMsg": true,
    "pasteImage.path": "${currentFileDir}/images/",
    "settingsSync.ignoredExtensions": [
        "liximomo.sftp",
        "wholroyd.jinja",
        "obkoro1.korofileheader",
        "autodesk.autolispext",
        "bungcip.better-toml",
        "thekalinga.bootstrap4-vscode",
        "hollowtree.canvas-snippets",
        "qingpeng.common-lisp",
        "redhat.fabric8-analytics",
        "grapecity.gc-excelviewer",
        "tootone.org-mode",
        "sophisticode.php-formatter",
        "tomoki1207.pdf",
        "msjsdiag.debugger-for-chrome"
    ],
    "explorer.confirmDelete": false,
    "explorer.confirmDragAndDrop": false,
    "workbench.editor.enablePreview": false,
    "[python]": {
        "editor.formatOnType": true
    },
    "git.confirmSync": false,
    "emmet.includeLanguages": {
        "wxml": "html"
    },
    "minapp-vscode.disableAutoConfig": true,
}