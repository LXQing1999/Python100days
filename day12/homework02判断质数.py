"""
homework02判断质数
判断正整数是不是质数
Author:25423
Date:2023/6/12
"""

# 括号里的num:int是类型标注
# ->bool输出的是bool类型

def is_prime(num:int)->bool:
    # 当数据特别大时,这个上限可以开个方向上取整更简单.
    # 强制类型转换和c++中是一样的
    for i in range(2,int(num**0.5)+1):
        if(num%i)==0:
            return False\
# 1不是质数,如果num为1 返回false 如果不为1 返回true
    return  num!=1

# 尝试一下调用函数
for n in range(2,100):
    if is_prime(n):
        print(n,end=' ')