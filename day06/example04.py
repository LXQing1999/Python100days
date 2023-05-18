"""
example04  强制类型转换
ord()查看字符对应的编码
chr 就是char
hex十六进制
Author:25423
Date:2023/5/18
"""
print(hex(ord('旭')),hex(ord('青')))
# 汉字的ASCII码范围
for i in range(0x4e00,0x9fa6):
    print(chr(i),end=' ')


