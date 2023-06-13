"""
homework01随机验证码
写一个生成指定长度的随机验证码，由数字和英文字母构成的函数
snake case  python标识符命名风格
Date:2023/6/11
"""
import random
import string

# 如果没有特别指定,默认长度就是4 要是有指定就按指定的来
def get_captcha_code(length=4):
    '''生成随机验证码'''
    selected_chars=random.choices(string.digits+string.ascii_letters,k=length)
    # 把选中的字符用空格连起来
    return ' '.join(selected_chars)

n=int(int(input('验证码长度:')))
for _ in range(10):
    print(get_captcha_code(n))
