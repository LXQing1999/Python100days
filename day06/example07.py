"""
example07 排序
Author:25423
Date:2023/5/19
"""
num1 = ['1', '10', '234', '2', '35']
# 按字符串排序
print(num1)
# 强制类型转换成int排序
num1.sort(key=int)
print(num1)

# 简单选择排序 每次从剩下的元素中选择最小的
num2 = [56, 78, 12, 34, 98]
# sorted_nums = []
for i in range(len(num2)-1):
    min_value,min_index = num2[i], i
    # 每一轮找到最小的值，并记下它的位置
    for j in range(i+1, len(num2)):
        if num2[j] < min_value:
           min_value, min_index = num2[j],j
    # 将最小的值放到最前面
    # Python里面交换数据的数据的时候居然不需要暂存吗
    # for循环完成后，将最小的值放到最终位置上
    num2[i], num2[min_index] = num2[min_index], num2[i]
print(num2)
'''
while len(num2)>0:
    sorted_nums.append(min(num2))
    num2.remove(min(num2))
'''
