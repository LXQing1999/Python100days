"""
example06 列表反转和排序
Author:25423
Date:2023/5/18
"""
fruits=['banana', 'dragon fruit', 'apple', 'strawberry', 'apple', 'cherry']
# 生成了一个新列表，并没有修改原来的列表
print(fruits[::-1])
# 原有的列表，没有被修改
print(fruits)

# 排序 默认是升序
fruits.sort()
print(fruits)
# 修改reverse 控制升序降序
fruits.sort(reverse=True)
print(fruits)