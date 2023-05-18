"""
example02 
Author:25423
Date:2023/5/18
"""
# 合并
list5=[1,3,5,7]
list6=[4,4,8]
longlist=list5+list6
list5+=list6
print(longlist)
print(list5)

# 比较 range([起，尾)，步长)
list7=list(range(1,8,2))
print(list7)
list8=[1,3,5,7]
print(list7==list8) # bool运算
print(list7!=list8) # bool运算

# 比较大小的时候是挨个比较的
list9=[1,3,5,7,9]
list10=[1,3,5,9]
print(list9>list8) # bool运算
print(list10>list8) # bool运算