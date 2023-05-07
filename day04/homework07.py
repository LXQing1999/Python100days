"""
homework07
找到1到10000之间的完美数（除自身之外的所有因子之和等于这个数
6=1+2+3
Author:25423
Date:2023/5/6
"""
import time
start =time.time()
for i in range(1,10001):
    sum = 0
    for j in range(1,int(i**0.5)+1):
# (i**0.5)相当于是开方，极大的提高了运行速度
#   for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        print(i)
end=time.time()
print(f'执行时间：{end-start:.3f}秒')