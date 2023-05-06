"""
example10 找到两个正整数的最大公约数
Author:25423
Date:2023/5/4
"""
x=int(input('x= '))
y=int(input('y= '))

while y%x!=0 :
    # temp=y
    # y=x
    # x=temp%x
    x,y=y%x,x      # 欧几里得算法
print(x)
'''

for i in range(x,0,-1):
    if(x%i==0) and (y%i==0):
        print(i)
        break'''