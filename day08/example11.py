"""
example11 
Author:25423
Date:2023/5/23
"""
import random
import string

# string.ascii_letters表示所有的大小写字母，而string.digits表示所有的数字。
all_chars=string.ascii_letters+string.digits

for _ in range(10):
# random.choices()从给定的序列中随机选择指定数量的元素，并以列表形式返回这些元素。
# random.choice单数，默认只取一个一个元素
# 可迭代对象
    selected_chars =random.choices(all_chars,k=4)
    print(' '.join(selected_chars))
'''在Python中，列表和数组是不同的数据类型。
列表是Python内置的一种数据类型，它是一种动态可变的序列，可以包含不同类型的元素，如数字、字符串、列表等。
列表使用方括号[]定义，可以通过索引访问元素，也可以使用各种方法对列表进行操作。
而数组则不是Python内置的数据类型，需要通过第三方库（如NumPy）来实现。数组是一种用于存储同一类型数据的数据结构，它可以是一维、二维或多维的。
与列表不同，数组的大小是固定的，一旦创建就无法改变。
数组中的元素可以通过索引访问，也可以使用各种方法对数组进行操作。
因此，列表和数组的主要区别在于它们的存储方式、元素类型和大小，以及对它们的操作方式。
在Python中，列表通常用于存储不同类型的元素，而数组则更适合用于数值计算和科学计算等领域。'''