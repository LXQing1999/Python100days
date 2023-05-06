"""
example02    分段函数求值  构造多分支结构
Author:25423
Date:2023/5/4

不要嵌套太多层，看着累
同一个缩进就是同一个代码块
"""
x = float(input('x= '))

if (x > 1):
    y = 3 * x - 5
if (-1<=x <= 1):
    y = x + 2
if(x<-1):
    y = 5 * x + 3
print(f'f(x)={y}')


if (x > 1):
    y = 3 * x - 5
else:
    if x<-1:
        y = 5 * x + 3
    else:
        y = x + 2
print(f'f(x)={y}')
