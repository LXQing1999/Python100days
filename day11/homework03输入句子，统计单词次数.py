"""
homework03输入句子，统计单词次数 
Author:25423
Date:2023/6/5
"""
# you are the apple of my eye.my lover.
sentence=input('请输入：').lower()
# split()默认是按空格拆分
words=sentence.replace(',',' ').replace('.',' ').split()
# 创建一个空字典，用于后续记录每个单词出现的次数。
counter_dict={}
# 字典的索引运算如果放在复制运算符的左边，要么是新增，要么是更新
# 这种写法偏c++ 我更习惯用这个
for word in words:
    if word in counter_dict:
        counter_dict[word]+=1
    else:
        counter_dict[word]=1
'''
# 获取字典counter_dict中键为word的值，如果键不存在则返回0 。
# 如果word存在则加1，并将值返回counter_dict[word]
for word in words:
    counter_dict[word]=counter_dict.get(word,0)+1
'''
# 根据单词出现的次数从高往低排序
# counter_dict.get用于获取字典中指定键的值。
# key=counter_dict.get表示按照字典中键对应的值进行排序。
# reverse=True表示从高到低排序
# 根据值来排序的，sorted完，返回的是键
sorted_keys=sorted(counter_dict,key=counter_dict.get,reverse=True)
# Python只对键进行排序，排序后，只有字典中的键被排列，而对应的值并没有被改变。
# 通过counter_dict[key]来获取每个键对应的值
# 打印出来sorted_keys里面只存了key
print(sorted_keys)
for key in sorted_keys:
    print(f'{key}:{counter_dict[key]}次')