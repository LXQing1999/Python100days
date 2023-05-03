"""
example12
输入三角形的三条边的长度，判断能否构成三角形
规则：任意两边的长度和大于第三边
Author:25423
Date:2023/5/3
"""
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
print(a + b > c and b + c > a and a + c > b)
