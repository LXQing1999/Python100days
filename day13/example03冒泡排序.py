"""
example03冒泡排序
设计函数的时候,一定要注意函数的无副作用性,调用函数不影响调用者
Author:25423
Date:2023/6/14
"""
def bubble_sort(items:list,ascending=True)->list:
    # 重新暂存一下,不改变原本的items数据
    items=items[:]
    for i in range(1,len(items)):
        swapped=False
        for j in range(0,len(items)-i):
            if items[j]>items[j+1]:
                items[j], items[j + 1]= items[j + 1], items[j]
                swapped =True
        if not swapped:
            break
    if not ascending:
        items=items[::-1]
    return items

if __name__ =='__main__':
    nums=[35,96,12,78,56,64,39,80]
    print(bubble_sort(nums,ascending=False))
    print(nums)
    words=['apple','god']
    print(bubble_sort(words, ascending=False))