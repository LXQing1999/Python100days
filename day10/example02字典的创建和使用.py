"""
example02字典的创建和使用
键值对 通过‘键’索引运算来获取值
键是不可变的数据类型
Author:25423
Date:2023/5/24
"""
student = {'id': 1001, 'name': 'lee', 'gender': 'male',
           'score': [90, 89, 100],
           }
# 构造器函数
student2=dict(id=1002,name='wong',gender='male')
print(student)
print(student2)
print(len(student))
# 只遍历了键
for key in student:
    print(key, student[key])
for key in student.keys:
    print(key)

# 只遍历了值
for value in student.values():
    print(value)
# 取出二元组,遍历了键值对
for x in student.items():
    print(x)
# 列表：提前放进列表里了
list1=[i for i in range(1,10)]
print(list1)
set1={i for i in range(1,10)}
print(set1)
dict1={i:i**2 for i in range(1,10)}
print(dict1)

# 生成器 临时通过运算给出的 可以一个一个的拿
gen_obj=(i for i in range(1,10))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
'''
for value in gen_obj:
    print(value)
'''