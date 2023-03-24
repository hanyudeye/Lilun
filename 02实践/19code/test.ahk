Active(t){
   WinActivate,ahk_exe %t%
   return
}
 
;激活资源管理器
#e::WinActivate,ahk_class CabinetWClass
;激活edge
#w::Active("msedge.exe")
;激活code
#c::Active("Code.exe")
