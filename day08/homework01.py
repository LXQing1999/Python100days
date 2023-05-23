"""
homework01 一个列表中有很多重复元素，写一段代码去掉列表中的重复元素
Author:25423
Date:2023/5/22
"""
items=[15,12,24,65,98,56,84,75,67]
unique_items=[]

for item in items:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)