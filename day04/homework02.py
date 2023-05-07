"""
example01  反转数字
Author:25423
Date:2023/5/6
"""
n=int(input('n= '))
total=0;
while n>0:
    total=total*10+n%10
    n=n//10     # 记得除号要打两个，和普通的/区分开
print(total)