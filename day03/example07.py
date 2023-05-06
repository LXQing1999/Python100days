"""
example07 求1到100之间3或者5的倍数的和
Author:25423
Date:2023/5/4
"""
sum=0
for i  in  range(1,101,1):
    if(i%3==0 or i%5==0):
        sum+=i
    else:
        pass
print(f'sum= {sum}')