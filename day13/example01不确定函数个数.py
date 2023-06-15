"""
example01不确定函数个数
在设计函数的时候,函数参数的诶个数是暂时无法确定的
位置参数  关键字参数
Author:25423
Date:2023/6/14
"""

# *是打包操作,多少个值都可以正常输入,相当于一个向量
# argument  参数
def add (*args,**kwargs):
    # 生成式语法
    temp=[arg for arg in args if(type(arg)in(int,float))]
    print (sum(temp))
    total = 0
    for value in kwargs.values():
        if type(value)in (int,float):
            total +=value
    return total

    '''
    total=0
    for arg in args:
        # 判断一下,就自动跳过不符合的元素
        if(type(arg) in(int ,float)):
            total+=arg
    print(total)
    return'''
   # print(args,type(args))
   # return sum(args)

add(1,2,'3',4)
add(5,7,'8',8,3,6)
add(3,6)
# 函数可以直接赋值给变量
fn=add
print(fn(5,7,'8',))