"""
example03 列表相关操作  比较
Author:25423
Date:2023/5/18
"""
# 比较的是字符的ASCII码
print(ord('b'))
print(ord('z'))
# 转二进制
print(bin(ord('b')))
# 字符串比较是从左向右逐个比较
print('banana'<'zoo')
print('banana'<'bbc')
# 一般不会比较两个类型不一样的元素
print(ord('张'))
print(ord('李'))
print('张三'<'李四')

