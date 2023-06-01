"""
example04字典 
Author:25423
Date:2023/6/1
"""
dict1={'A':100,'B':200,'C':300}
dict2={'D':400,'E':500,'F':600}
# 更新 （元素的合并或更新）
dict1.update(dict2)
print(dict1)
# 删除 必须是存在的值，不然会error
dict1.pop('B')
print(dict1)
# pop掉最后面（上面）的元素
dict1.popitem()
print(dict1)
# 更新/添加字典的值
# 键在字典中，就更改值
# 键不在字典中，就添加键值对
dict1.setdefault('C',666)
dict1.setdefault('G',999)
print(dict1)

# 清空
dict1.clear()
print(dict1)