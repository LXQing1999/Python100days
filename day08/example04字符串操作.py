"""
example03字符串操作
str是不可变类型
Author:25423
Date:2023/5/22
"""
a='Hello,World'
c='l'
# 大写
b=a.upper()
print(b)
# 小写
print(b.lower())
print(b.capitalize())
print(b.title())

# 判断a是由数字构成的吗
print(a.isdigit())
# 判断a是由字母构成的吗
print(a.isalpha())
# 判断a是由字母和数字构成的吗
print(a.isalnum())
# 判断a是ascii码表示的吗
print(c.isascii())
print(a)
c='你好'
print(c.isascii())
