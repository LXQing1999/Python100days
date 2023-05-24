"""
exaple03
顺序存储：随机存储，查找元素效率低
hash存储：时间复杂度常量级
可变容器（列表、集合、字典）都不能hash，因此都不能放到集合中，作为集合的元素
Author:25423
Date:2023/5/24
"""
set1={'apple','banana','cherry','gobi'}
set2={True,False,True,True,False}
print(set1)
print(set2)
# 注意在hash存储中，元素是没有顺序的
set1.add('grape')
print(set1)
# 删除的元素也是随机的,因为集合是无所谓顺序的
print(set2.pop())
# 删除指定元素
set1.discard('gobi')
print(set1)
# list是不可散列hash的类型
# 集合底层使用了高效率的存储方式，散列存储
# 联系一下数据结构的内容，集合会构造一个hash函数，可以根据地址实现随机存取
# 尽量让不同的元素产生不同的hash码
# 查找效率远高于列表（顺序存储）
'''
set3={[1,2,3],[4,5,6]}
print(set3)'''