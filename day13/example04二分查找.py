"""
example04二分查找 
Author:25423
Date:2023/6/14
"""
import random
items=[random.randrange(1,100) for _ in range(10) ]
start,end=0,len(items)-1

def bin_search(items:list,key)->int:
    start,end=0,len(items)-1
    while start<=end:
        mid=int((start+end)/2)
        if key>items[mid]:
            start=mid+1
        elif key<items[mid]:
            end=mid-1
        else:
            return mid
    return -1
# 确保被调用时,不会再被输出一边
# 直接敲main 然后tab补齐
if __name__ =='__main__':
    print(items)
    print(bin_search(items,7))
    print(bin_search(items,22))

