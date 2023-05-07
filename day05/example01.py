"""
example01 掷骰子
Author:25423
Date:2023/5/7
"""
import random
# f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0
f1= f2=f3=f4=f5=f6 = 0
for i in range(6000):
    face = random.randrange(1, 7)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f1, f2, f3, f4, f5, f6)