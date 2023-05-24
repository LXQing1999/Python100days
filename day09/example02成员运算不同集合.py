"""
example02 成员运算
Author:25423
Date:2023/5/23
"""
set1={1,2,3,4,5}
set2={2,4,6,8}
# 成员运算 确定性 元素要么在集合中，要么不在集合中
# 集合的成员运算在效率上是远远高于列表的成员运算
print(1 in set1)
print(1 not in set1)

# 交集
print(set1&set2)
# intersection交接（点或线），相交；交汇点（尤指道路）；（动作）交接，交叉
print(set1.intersection((set2)))
# 并集
print(set1|set2)
print(set1.union(set2))
# 差集
print(set1-set2)
print(set1.difference(set2))
# 对称差 ：两个集合的并集减去它们的交集  （就是抠掉相交的那一块）
print(set1^set2)
print((set1|set2)-(set1&set2))  # 这个比较好记
print((set1.symmetric_difference(set2)))

set3={1,2,3,4,5,6,7,8,9}
# 判断真子集 ：A包含于B,且A不等于B,就说集合A是集合B的真子集
print(set1<set3)
# 判断子集：如果集合A的任意一个元素都是集合B的元素，那么集合A称为集合B的子集。
print(set1<=set3)
# 判断超集:超集就是子集的反义词
print(set1>set3)
