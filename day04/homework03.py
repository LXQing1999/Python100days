"""
homework04 求阶乘
A(m,n)=m!/(m-n)!  排列
C(m,n)=m!/n!/(m-n)!  组合
Author:25423
Date:2023/5/6

as ->alias 别名
"""
# 从math模块导入函数factorial，并重命名为f
from math import factorial as f
m=int(input('m= '))
n=int(input('n= '))
print(f(m)//f(n)//f(m-n))


'''
import math
m=int(input('m= '))
n=int(input('n= '))

print(math.factorial(m)//math.factorial(n)//math.factorial((m-n)))'''


'''
传统方法
fm=1
for i in range(2,m+1):
    fm*=i

fn=1
for i in range(2,n+1):
    fn*=i

fk=1
for i in range(2,m-n+1):
    fk*=i

print(fm//fn//fk)
'''