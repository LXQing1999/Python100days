"""
example10加密
对称加密
非对称加密
Author:25423
Date:2023/5/23
"""
message='attack at dawn.'
# 生成字符串的转换的对照表
table=str.maketrans('abcdefghijklmnopqrstuvwxyz',
                    'defghijklmnopqrstuvwxyzabc')
# 通过字符串的translate方法实现字符串转译
print(message.translate(table))