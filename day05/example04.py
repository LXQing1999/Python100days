"""
example04     将一枚骰子投掷60000次，统计每一面出现的次数
Author:25423
Date:2023/5/7
"""
import random
# fs=[0,0,0,0,0,0]
fs =[0]*6
for i in range(60000):
    face=random.randrange(1,7)
    fs[face-1]+=1
print(fs)  # 输出数组的时候直接print数组名就行了

# 前面这个i是枚举的序号，后面这个value是对应的数组元素
for i,value in enumerate(fs):
    print(f'{i+1}点摇出了{value}次')

