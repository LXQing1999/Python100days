"""
example06center 
Author:25423
Date:2023/5/22
"""
a='An apple a day,keep doctor away!'
# 其他的空位用'$'补齐，默认是空格
print(a.center(80,'='))
print(a.rjust(80,'='))
print(a.ljust(80,'='))

b='123'
print(b.zfill(6))
c=1234
d=345
# 零填充（在左边补0）
print(b.zfill(6))
# format:格式化  字符串
print(f'{c}+{d}={c+d}')
print('%d+%d=%d'%(c,d,c+d))
print('{}+{}={}'.format(c,d,c+d))
# 再次使用format方法，但这次我们指定了变量插入的位置。
# 将c+d作为第一个变量插入，c作为第三个变量插入，d作为第二个变量插入。因此输出结果为'1579+345=1234'。
# :.2f 是保留两位小数
print('{2}+{1}={0:.2f}'.format(c,d,c+d))

