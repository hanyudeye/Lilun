import time

def func():
    time.sleep(1)
    a=time.perf_counter()#第一次调用per_counter,所以a值应该为零,但是他不是刚好为零
    print(a)
    print(round(a))#把a四舍五入验证下
    print(type(a))#验证a是浮点数
    time.sleep(5)
    b=time.perf_counter()#sleep5秒后,b的值就应该是5
    print(b)
func()