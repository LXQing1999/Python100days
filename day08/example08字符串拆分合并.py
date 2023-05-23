"""
example08字符串拆分合并
r-前缀就是reverse的意思，翻转。就是倒着从右往左数
split 把字符串进行拆分
join 把字符串连接起来
Author:25423
Date:2023/5/22
"""
song1 = 'I have a pen,I have an apple.'
song2 = (song1.replace(',', ' ')).replace('.', ' ')
# 用空格拆分字符串得到一个列表
# split默认是通过空格拆开的
print(song2.split())
words1 = song2.split()
for word in words1:
    print(word)

# 空格拆分字符串，最多允许拆分3次
words2 = song2.split(' ', maxsplit=3)
print(words2, len(words2))

# ,拆分字符串，不限制拆分次数
song3 = song1.split(',')

for x in song3:
    print(x)

# 用指定的字符串将字符串连接起来
poem = ['Where have you been', 'Where did you go']
print('?'.join(poem))

