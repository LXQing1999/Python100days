"""
example05 插入、索引、计数、删除、清空元素
Author:25423
Date:2023/5/18
"""
fruits=['banana','apple','strawberry','apple']
fruits.append('cherry')
fruits.insert(1,'dragon fruit')  # （插入的位置，元素）
print(fruits)

# 索引 默认是从左往右索引，返回下标
print(fruits.index('strawberry'))
print(fruits.index('apple'))
# 从下标3的位置往右找
print(fruits.index('apple',3))
if 'apple' in fruits[3:]:
    print(fruits.index('apple', 3))

# 计数
print(fruits.count('apple'))

# 删除元素
fruits.pop() # 弹出最后一个元素
print(fruits)
fruits.pop(1) # 删除的元素
print(fruits)

del fruits[0]
print(fruits)
while 'apple' in fruits:
    fruits.remove('apple') # 删除列表中，第一次出现的元素
print(fruits)

# 清空列表元素
fruits.clear()
print(fruits)