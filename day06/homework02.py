"""
homework02
向列表中添加10个随机整数，找出其中第2大的元素
random.random()随机取值在[0,10)之间
temp=random.random()*（b-a) +a   # 要求取[a,b)之间的数
Author:25423
Date:2023/5/16
"""
import random
# nums=[]
# for _ in range(10):  # 左闭右开，包括0，不包括100
#     temp=random.randrange(1,100)   # Fn + F1可以打开pcharm在线文档
#     nums.append(temp)    # 将随机数加到列表中

# 列表的生成式语法  推导式  Python中有专门的操作来解释
nums=[random.randrange(1,100) for _ in range(10)]
print(nums)

m1,m2=nums[0],nums[1]
if m1<m2 :
    m1,m2=m2,m1
for i in range(2,len(nums)):
    if nums[i]>m1:
        m1,m2=nums[i],m1
    elif nums[i]==m1:
        continue
    elif nums[i]>m2:
        m2=nums[i]
print(m2)

