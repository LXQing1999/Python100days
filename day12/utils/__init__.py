"""
__init__.py
包的初始化文件 传入一个文件名 返回这个文件的后缀名\
123.py   py/.py
123.py.txt   txt/.txt
.abc   没有后缀名 返回空字符串
abc.   没有后缀名  返回空字符串
Author:25423
Date:2023/6/14
"""
# 传入文件名  判断是否有点.   返回后缀
# 定义函数时,写在*前面的函数称为位置参数,调用函数传参时,只需要对号入座
# 写在*后面的参数,称为命名关键字参数,调用参数传递参数时,必须写成  参数名=参数值  的形式
def get_suffix(filename:str,*,has_dot:bool=False)->str:
    position=filename.rfind('.')
    # 如果不需要点
    if not has_dot:
        position=position+1

    # 三元运算 python特有的
    return filename[position+1:] if position>0 else ' '

    '''
    if position>0:
        return filename[position+1:]
    return ' '           '''