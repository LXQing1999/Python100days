"""
example09
有15个男人和15个女人坐船出海，船坏了，需要把其中15个人扔到海中，其他人才能活下来；
所有人围成一圈，由某个人从1开始依次报数，报到9的人被扔到海里，下一个人重新从1开始报数，
直到将15个人扔到海里。最后15个人女人都幸存下来，15个男人被扔进了海里，15个男人都被扔进了海里。
问原先哪个位置是男人，哪个位置是女人。

救命，这是什么鬼题目啊！
Author:25423
Date:2023/5/19
"""
person=[i for i in range(1,31)]
print(person)
# 将列表person的第9个元素到最后一个元素放到最前面
# 列表person的第1个元素到第8个元素交换位置放到后面
# 注意一下这个切片操作是左闭右开的
# 第9个元素的值是10，它并没有被“踢出”列表，而是被移动到了列表的最前面。
for _ in range(15):
    # ！！！person[:8]右边是开区间，所以第8个元素，也就是9被排除在外了
    person=person[9:]+person[:8]
    print(person)
print(person)
# 代码使用for循环，遍历1-30的数字，如果这个数字在列表person中，就输出‘女’，否则输出‘男’。
for i in range(1,31):  # 左闭右开
    print('女' if i in person else '男',end=' ')
'''
person=[True]*30
index,counter,num=0,0,0
while counter<15:
    if person[index]==True: # 没被扔进海里 继续报数
        num+=1
        if num==9:
            person[index]=False
            counter+=1  # 记录累计扔了几个人了
            num=0  # 报数归零
    index+=1  # 从下一个人开始计数
    if index ==30:
        index=0  # 防止超出
print(person)

# 三元条件运算,如果是真的，就选择前面的女，假的就输出前面的男
for i in person:
    print('女'if i else'男', end=' ')
'''


'''
for i in person:
    if i:
        print('女',end=' ')
    else:
        print('男', end=' ')
'''