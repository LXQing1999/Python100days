"""
example02 元组 不可变的容器
YNG
Author:25423
Date:2023/5/20
"""
# 不要漏掉,
# 注意一下，如果是[ ]的话，是数组，如果是( )的话，是元组
fruits1 = ('banana', 'dragon_fruit', 'pineapple', 'peach','apple')
print(type(fruits1))
# 重复运算
print(fruits1 * 3)
# 成员运算
print('apple' in fruits1)
# 合并运算
fruits2 = ('strawberry', 'cherry')
fruits3= fruits1 + fruits2
print(fruits3)

# 索引和切片   -1是最右边的那个
print(fruits3[1],fruits3[-1])
# 元组不可以赋值

print(fruits3[1:4])   # 左闭右开
print(fruits3[1:4:2])  # 步长为2
print(fruits3[::-1])  # 反转

print(fruits3.index('banana'))
print(fruits3.count('banana'))

# 'tuple' object has no attribute 'append'
# print(fruits3.append('orange'))