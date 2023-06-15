"""
example04 
Author:25423
Date:2023/6/14
"""
import utils

print(utils.get_suffix('hello.py'))
# 调用函数传递参数时,
print(utils.get_suffix(has_dot=True,filename='hello.py'))
print(utils.get_suffix('hello.py.txt'))
print(utils.get_suffix('hello.py.txt',has_dot=True))
print(utils.get_suffix('hello'))
print(utils.get_suffix('.hello'))