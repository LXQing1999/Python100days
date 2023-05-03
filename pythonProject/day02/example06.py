"""
example06
Author:25423
Date:2023/5/3
"""
a1 = float(input('a1= '))
b2 = float(input('b2= '))
# 如果不写这个int( )编译器默认输入的是字符

print(a1, '+', b2, '=', a1 + b2)
print('%.1f - %.1f=%.1f' % (a1, b2, a1 - b2))
print('%.2f * %.2f=%.2f' % (a1, b2, (a1 * b2)))
print('%.3f // %.3f=%.3f' % (a1, b2, a1 // b2))  # 整数除法
print('%f/%f=%f' % (a1, b2, a1 / b2))
print('%f %% %f=%f' % (a1, b2, a1 % b2))
print('%f ** %f=%f' % (a1, b2, a1 ** b2))
# 前面那些%f是占位符
