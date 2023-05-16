"""
homework01 输入三个整数，按照从大到小的顺序输出
Author:25423
Date:2023/5/16
"""
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))

if a<b :
    a,b=b,a
if a<c :
    a,c=c,a
if b<c :
    b,c=c,b

print(a,b,c)
import random
# nums=list()
# print(nums)
# for _ in range(10):  # 左闭右开，包括0，不包括100
#     temp=random.random()   # Fn + F1可以打开pcharm在线文档
#     nums.append(temp)    # 将随机数加到列表中
nums=[]
for _ in range(10):  # 左闭右开，包括0，不包括100
    temp=random.randrange(1,100)   # Fn + F1可以打开pcharm在线文档
    nums.append(temp)    # 将随机数加到列表中
# max_value=max(nums)
# # 通过remove操作从列表中删除指定的元素
# nums.remove(max_value)
# print(max(nums))
# print(nums)
max_value=nums[0]
for i in range(1,len(nums)):
    if nums[i]>max_value :
        max_value=nums[i]
print(max_value)