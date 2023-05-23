"""
example05字符串的操作
正着找和倒着找的区别
index \ rindex
find \ rfind
Author:25423
Date:2023/5/22
"""
a='An apple a day,keep doctor away! apple '
# 返回了Apple的位置 默认从0最左侧开始找
print(a.index('apple'))
# index(目标,新起点)重新确定了查找起点，找不到就崩溃not found
print(a.index('apple',10))
print(a.rindex('apple'))
# 找不到不会崩溃，返回-1
print(a.find('apple'))
print(a.rfind('apple'))