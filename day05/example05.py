"""
example05
输入10个整数，计算平均值、方差和标准差，找出最大值和最小值
描述型统计 ：通常用于可以获得总体的情况
推断型统计，只能获得样本，通过样本去推测总体
Author:25423
Date:2023/5/7
"""
nums = []
for i in range(10):
    temp = int(input('请输入数据： '))
    nums.append(temp)
mean_value = sum(nums) / len(nums)
total = 0
for num in nums:
    total += (num - mean_value) ** 2
variance_value = total / (len(nums) - 1)  # 方差variance_value
std_value=variance_value**0.5  # 标准差
max_value, min_value = max(nums), min(nums)
print(f'均值：{mean_value}')
print(f'方差：{variance_value}')
print(f'标准差：{std_value}')
print(f'极差：{max_value-min_value}')