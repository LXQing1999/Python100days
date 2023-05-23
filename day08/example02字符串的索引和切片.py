"""
example02 字符串的索引和切片
Author:25423
Date:2023/5/22
"""
a='hello,world'
# 默认是从左往右数的，加上负号是从右往左数的
# -1就是倒数第一个  -len就是倒数第len个，也就是第一个
print(a[0],a[-len(a)])
print(a[len(a)-1],a[-1])

# a[起：终：步长]
print(a[0:5])
print(a[0:5:2])
# a[::-1]逆向
print(a[::-1])