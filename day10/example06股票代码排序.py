"""
example06股票代码排序
找到股票价格大于100的，生成一个新的字典
找出价格最高的最低的股票对应的股票代码
按股票价格高低，给股票排序
Author:25423
Date:2023/6/3
"""
stocks={'AP':191.88,'GDO':1186.96,'GE':668.46,'FB':208.4}
new_stocks={}
# item就是stocks的键值对，要熟悉Python的写法
# 居然可以直接把for循环写在里面
new_stocks={key:value for key,value in stocks.items() if value>100}
print(new_stocks)
# Python中的max可以应对多种情况
print(max(stocks.values()))
words=['apple','bus','car','zoo','internet','of']
# 默认是按字母表排序的，但可以通过修改key的值，实现不同的排序方案
print(max(words))
print(max(words,key=len))
print(min(words,key=len))
# sort()默认也是按照字母表排序的，key可以调整
words.sort(key=len)
print(words)
# 通过键来取值
#keys=['AP','GDO','GE','FB']
print(max(stocks,key=stocks.get))
print(min(stocks,key=stocks.get))
# 默认升序，通过比较值来给键排序
print(sorted(stocks,key=stocks.get))
print(sorted(stocks,key=stocks.get,reverse= True))
# zip把两组值压缩成一个二元组
for x in zip(stocks.values(),stocks.keys()):
    print(x)
for x in zip([1,2,3,4],'ABCD'):
    print(x)
# 将zip后的结果，直接创建成一个字典，并重命名为dict1
dict1=dict(zip('ABCD',[1,2,3,4]))
dict2=dict(A=1,B=2,C=3,D=4,E=5)
print(dict2)
dict3=dict(zip(dict1.values(),dict1.keys()))
print(dict3)
# 在二元组中用下标取到第二个元素
print(max(zip(stocks.values(),stocks.keys()))[1])
print(min(zip(stocks.values(),stocks.keys()))[1])
'''
for key,value in stocks.items():
    if value>100:
        new_stocks[key]=value
print(new_stocks)
'''