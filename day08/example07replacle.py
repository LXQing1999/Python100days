"""
example07
strip可以去掉左右两边的空格
Author:25423
Date:2023/5/22
"""
email='   56545 1999@qq.com  '
tel='  465 4654  '

print(email.strip())
print(tel.strip())
# 去掉左边\右边的空格
print(email.lstrip())
print(tel.rstrip())
# 将指定的字符串替换成新的内容
print(email.strip().replace('56545 ','LXQing').replace('qq','gmail'))