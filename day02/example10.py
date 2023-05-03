"""
逻辑运算的应用
Author:25423
Date:2023/5/3
"""

a = int(input('a= '))  # 输入一个整数a
flag1 = a > 50
flag2 = a % 2 == 0
print(flag1, flag2)
print(flag1 and flag2)
print(a > 50 and a % 2 == 0)
