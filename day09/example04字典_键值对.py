"""
example04字典_键值对 类似c++中的结构体
元素由键和值两部分组成。冒号前是键  冒号后的是值 合在一起叫键值对
Author:25423
Date:2023/5/24
"""
# students={'lee':'湖北','huang':'河南','wong':'新疆'}
# 在像 Python 这样的编程语言中，不允许在十进制整数文字中使用前导零。
# 例如，如果你写一个像 0123 这样的数字，它将被解释为八进制整数（基数 8）而不是十进制整数（基数 10）。这可能会导致代码错误。
# 键用了hash存储，键不可变
# 值
student = {'id': 1001, 'name': 'lee', 'gender': 'male',
           'score': [90, 89, 100],
           }
print(student['id'])
print(student['name'])

for i in student['score']:
    print(i)