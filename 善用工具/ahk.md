
## 激活某个class 下 特定标题的窗口

这里的class 是 vscode 的class Chrome_WidgetWin_1，但是浏览器也是这个窗口class

```
WinTitle=ahk_class Chrome_WidgetWin_1
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"Lilun")
		{
			;main_flag:=1
			main_id:=win.id
			;Hotkey,#z,bind
            WinActivate,ahk_id %main_id%
		}
}
return

```