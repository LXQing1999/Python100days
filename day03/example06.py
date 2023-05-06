"""
example06 
Author:25423
Date:2023/5/4
"""

print(sum(range(1,101)))

total1 = 0
for i in range(1, 101):
    total1 += i
print(total1)

total2 = 0
for i in range(1, 101):
    if (i % 2) == 0:
        total2 += i
    else:
        pass   # 相当于c中的continue
print(total2)

total3 =sum(range(1,101,2))
print(total3)