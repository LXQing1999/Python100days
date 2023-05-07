"""
example06 数字矩阵
Author:25423
Date:2023/5/6
"""
n=int(input('n= '))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=' ')
    print()   # 输出默认的换行

for i in range(1,n+1):
    for i in range(1,i+1):
        print(i,end=' ')
    print()   # 输出默认的换行