"""
example02    分段函数求值  构造多分支结构
Author:25423
Date:2023/5/4
"""
x=float(input('x= '))
if(x>1):
    y=3*x-5
elif(x>=-1):
    y=x+2
else:
    y=5*x+3
print(f'f(x)={y}')