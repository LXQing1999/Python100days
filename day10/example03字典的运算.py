"""
example 
Author:25423
Date:2023/6/1
"""
student = {'id': 1001, 'name': 'lee', 'gender': 'female',
           'score': [90, 89, 100],
           }
print(student)
# 更新字典中的值
student['name']='huang'
student['gender']='male'
print(student)
print('id'in student)
print('name'in student)
print('address'in student)
student['address']='河北'
print('address'in student)

print(student['name'])
# 这样写保证了，取不存在的键的时候，不会报错
# 比较稳妥的写法
print(student.get('age'))
# 删除键值对
del student['name']
# pop在删除前会返回该数据
student.pop('name')

print(student.get('name'))

# 如果要使用下标（索引）运算，那么一定要保证键一定存在
if 'id' in student:
    print(student['id'])