"""
homework01 水仙花数
各位数字的立方和，刚好等于这个数本身
153=1^1^1+5^5^5+3^3^3
Author:25423
Date:2023/5/6
"""
for num in range(100,1000):
    h=num//100
    d=(num//10)%10
    s=num %10
    if (h**3+d**3+s**3 ==num):
        print(num)