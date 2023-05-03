"""
homework01
输入圆的半径，计算圆的周长和面积
Author:25423
Date:2023/5/3
"""
import math

radius = float(input('请输入圆的半径： '))
perimeter = 2 * math.pi * radius
area=math.pi*radius**2
print(f'圆的周长：{perimeter:.4f}')
print(f'圆的面积：{area:.4f}')