"""
冒泡排序
两个相邻的元素挨个比较，大的放到后面去，直到比完一轮

Author:25423
Date:2023/5/19
"""
# nums = [56, 78, 12, 34, 98]
nums = [9, 2, 3, 7,8]
for i in range(1, len(nums)):
    flag = True
    for j in range(0, len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            flag=False
# 当一轮中没有任何元素交换位置后，那就是比完了
    if flag == True :
        break
print(nums)