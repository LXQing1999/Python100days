"""
example09编码解码
编码：把一种字符集转换成另一种字符集
utf-8 和 gbk是unicode万国码的常见实现方案，
通常都选utf-8各国语言通用
其他的编码方式各有缺陷
str 字符串 encode字符集  bytes 字节串
解码：需要编码和解码方法一致
utf-8是一种变长编码 表示数字和英文字母，只需要一个字符。表示中文需要三个字节；表示emoji需要4个字节
最好不用其他奇奇怪怪的保存中文，就用utf-8完事了
Author:25423
Date:2023/5/23
"""
a='你去过何处？Where have you been?'
# gbk是之前讲过的编码方式 还有ASCII码和GB2312
# gbk 是一种固定长度的中文编码格式
b=a.encode('gbk')  #  bytes 字节串
# utf-8可以表示世界上几乎所有的字符
b2=a.encode('utf-8')
print(type(b))
print(b,len(b))
print(b2,len(b2))
# decode解码
# 只有对应上才能正确解码
c=b'\xe4\xbd\xa0\xe5\x8e\xbb\xe8\xbf\x87\xe4\xbd\x95\xe5\xa4\x84\xef\xbc\x9f'
# 如果编码和解码的方式不一致，可能会出现异常或者乱码
# print(c.decode('gbk'))
print(c.decode('utf-8'))