"""
example02 容器型数据类型（用一个变量可以保存多个数据
列表list  元组tuple  集合set  字典dict
Author:25423
Date:2023/5/7
"""
nums = [10, 100, 1000]  # 列表
print(type(nums))
print(nums)
rules = ['热爱祖国’，'
         '‘热爱人民']
print(type(rules))
print(rules)
nums.append(10000)  # 在最后添上一个数据  追加元素
nums.insert(0,1)  # 在哪个位置之前加上哪个数  插入元素
print(nums)
rules.pop()  # 弹出最后一个元素
# 其实这个很好理解，c++中，数组名的本质是指针，所以可以弹出



