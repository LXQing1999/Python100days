"""
整数的表示法
"""
a = 110  # 默认是十进制
b = 0o110  # 八进制
c = 0x110  # 十六进制
d = 0b110  # 二进制

# 浮点数的科学计数法
e=123e-5    # 123乘以10的-5次方
print(a, b, c, d,e)

# 十进制转二进制
print(bin(47))
# 十进制转八进制
print(oct(47))
# 十进制转十六进制
print(hex(47))