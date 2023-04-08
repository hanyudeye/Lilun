; 测试ahk脚本

```
Numpad0 & Numpad1::
MsgBox You pressed Numpad1 while holding down Numpad0.
Return
```
; 使用 hotkey (Alt+~) 在同类窗口切换

\::
if WinActive("Window 1")
Send, {F2}

else if WinActive("Window 2")
Send, {F3}

else if WinActive("Window 3")
Send, {F4}

else if WinActive("Window 4")
Send, {F5}

else if WinActive("Window 5")
Send, {F6}

else if WinActive("Window 6")
Send, {F1}
return