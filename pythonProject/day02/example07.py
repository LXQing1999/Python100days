"""
example06
Author:25423
Date:2023/5/3
"""
a1 = float(input('a1= '))
b2 = float(input('b2= '))
# 如果不写这个int( )编译器默认输入的是字符

# f -format -格式化字符串
# 便捷语法
print(f'{a1}+{b2} ={a1+b2:.1f}')    # :.2f 保留两位小数
print(f'{a1}-{b2} ={a1-b2}')
print(f'{a1}*{b2} ={a1*b2}:.3f')
print(f'{a1}/{b2} ={a1/b2:.2f}')