"""
exmaple01 创建列表
Author:25423
Date:2023/5/16
"""
# 虽然可以吗，但是最好不要把不同类型的都放进一个数组里去

# 字面量语法
# list1=[1,2,3,1,1.1,'hello']
list1=['hello','apple','banana','orange']
print(list1)

# 构造器语法
list2=list(range(1,10))  # 构造器函数
print(list2)

# 生成式语法/推导式语法
list3=[i**2 for i in range(1,10)]
print(list3)

# 索引和切片
# 正向索引：0~N-1  负向索引：-N ~-1
# 遍历列表中的元素
for i in range(len(list1)):
    print(list1[i])
# 这样就是倒着取数
for i in range(-len(list1),0):
    print(list1[i])
# 数组名也可以放进for循环的
for x in list1:
    print(x)

# enumerate对列表进行预处理，得到下标和元素
for i,x in enumerate(list1):
    print(i,x)

# 和列表相关的运算
# 把列表里的东西重复五次
list4=[1,10,100]*5
print(list4)

# 成员运算
# bool运算，看10是否在List4中,返回true或false
print(10 in list4)
print(5 not in list4)
print('apple' in list1)
print('a' in list1)

