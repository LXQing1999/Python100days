"""
homework05 打印一到一百的质数
Author:25423
Date:2023/5/6
"""


# 注意2是质数哦

for num in range(2, 100):
    is_prime = True  # 全部假定是质数
    for i in range(2, num):
        if (num % i == 0):
            is_prime = False  # 不是质数
            break  # 跳出本层for循环
    if is_prime == True:
        print(num)
