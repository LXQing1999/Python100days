"""
example03 元组的应用
Author:25423
Date:2023/5/21
"""
a,b=(5,10),(2,8,6)
print(a)
print(b)

# Python里有专门的指令来处理交换
a,b=b,a
print(a)
print(b)
# 出现这种情况，最主要的原因是数组名的本质是指针
c,*d,e=5,10,15,8,17,21
print(c)
print(d)
print(e)

# 给没留指针的各存一个数据
*f,g,k=5,10,15,8,17,21
print(f)
print(g)
print(k)

# unpack解包指令
c,*d,e=*f,g,k
print(c,d,e)