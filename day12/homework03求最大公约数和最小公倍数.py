"""
homework03求最大公约数和最小公倍数
设计函数:一个函数单一职责,高内聚 ,识别清晰,易于维护
低耦合
函数封装那些相对独立的功能,到时候直接调用 结构体
Author:25423
Date:2023/6/12
"""

# 辗转相除法求最大公约数

def gcd(x:int ,y:int)->int:
    while y%x!=0:
        x,y=y%x,x
    return x
print(gcd(3,5))
print(gcd(12,15))

# 最小公倍数
def lcm(x:int ,y:int)->int:
    return x*y//gcd(x,y)
print(lcm(12,15))