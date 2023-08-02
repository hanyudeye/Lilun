# 冒泡排序


def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return  

alist=[1, 3, 2, 4, 5, 6, 7, 8, 9, 0]
bubble_sort(alist)
print(alist)
