"""
example02参数
*args 可变参数 可以接收零个或任意多个位置参数 将所有位置参数打包成一个元组
**kwargs 可以接收零个或任意多个关键字参数 将所有的关键字参数打包成一个字典
关键字参数一定是在位置参数的后面

Python中的函数是一等函数:
1.函数可以作为函数的参数
2.函数可以作为函数的返回值
3.函数可以赋值给变量

如果把函数作为函数的参数或者返回值 通常称为高阶函数
Author:25423
Date:2023/6/14
"""
import operator
# fn 一个实现二元运算的函数
# 传入了 初值参数 函数参数 位置参数 关键字参数
def calculate(*args,op,init_value=0,**kwargs):
    total=init_value
    for arg in args:
        if type(arg) in(int,float):
            total=op(total,arg)
    for value in kwargs.items():
        if type(value) in (int,float):
            total=op(total,value)
    return total

def add (x,y):
    return x+y

'''def mul (x,y):
    return x*y'''

def sub (x,y):
    return x-y
# 没有特别指明init_value默认是0
# print(calculate(11,22,33,44,op=add))
print(calculate(11,22,33,44,op=lambda x,y:x+y))
# lambda简化一句话的函数
print(calculate(11,22,33,44,init_value=1,op=lambda x,y:x*y))
# 在前面定义一个新函数也可以
fn=lambda x,y:x-y
print(calculate(11,22,33,44,op=fn,init_value=100))