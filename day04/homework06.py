"""
homework06   输入三角形三边长度能否构成三角形
Author:25423
Date:2023/5/6
"""
import math
while True:
    a = float(input('a= '))
    b = float(input('b= '))
    c = float(input('c= '))
    if a * b * c == 0: break
    if (a + b > c and a + c > b and b + c > a):
        print('正确')
        per = a + b + c
        p = (a + b + c)/2
        # 海伦公式求面积    开根号(p (p-a) (p-b) (p-c))
        A = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(f'面积为{A:.2f}')
        print(f'长度为{per}')
    else:
        print('重新输入')
