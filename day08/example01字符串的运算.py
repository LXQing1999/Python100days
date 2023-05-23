"""
example01 字符串的运算
实际上比较的是字符编码 比如ASCII编码的大小
联系一下计组就知道了
字符串不能二次修改的，只能读，和C++是一样的
Author:25423
Date:2023/5/22
"""
a='hello, world'
b=a+'!!!'
print(b)
# 空格也计数
print(len(a))
# 在C语言中，字符串和数组其实是等价的，都是一系列连续的内存单元，存储数据。
for i in range(len(a)):
    print(a[i],end=' ')
print('\n')
print(a*5)
print('hello' in a)
print('bye' in a)

b='hello,world'
print(a==b)
print(a!=b)

# 是从左向右比较ascii码的大小，一旦比出来直接返回，不用再往后比了
c='bye'
print(b>c)

d='hello,boy'
print(b>=d)

print(ord('L'),ord('l'))