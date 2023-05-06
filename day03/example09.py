"""
example09 计算阶乘
Author:25423
Date:2023/5/6
"""
n=int(input('n= '))
total=1
for i in range(2,n+1):   # 注意是左开右闭的
    total *=i
print(f'{n}!={total}')
