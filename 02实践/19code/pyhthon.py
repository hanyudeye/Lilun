def xx():
    print ("hello", " world")


# 正则表达式
import re
def reg():
    match="foo"
    str="foonihao,foo"
    r=re.match(match,str)
    print(r.group())


if __name__=="__main__":
    # print(_name__)
    # print(__loader__)
    # xx()
    # print("azzczzzb"[2:-2])
    reg()

