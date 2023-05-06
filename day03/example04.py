"""
example04  累进税
Author:25423
Date:2023/5/4
"""
total = float(input('本月收入： '))
insurance = float(input('五险一金扣除： '))

E = total - insurance
I = E - 3500
if 0<I<1500:
    R=0.03
    D=0
elif I<4500:
    R=0.1
    D=105
elif I<9000:
    R=0.2
    D=555
elif I<35000:
    R=0.25
    D=1005
elif I<55000:
    R=0.3
    D=5505
else:
    R=0.45
    D=13505
if I>0:
    T=I*R-D
else:
    T=0
print(f'应纳税款：{T:.2f}元')
