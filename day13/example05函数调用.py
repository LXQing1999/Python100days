"""
example05函数调用
settings\File | Settings | Editor | Live Templates 可以自己定义模板
联系一下计组,有保存现场 调用函数 恢复现场的过程
每个函数都有自己的栈结构 保存现场就是将整个栈结构保存起来

函数如果直接或间接的调用了自身 这叫做递归调用
无休止的调用会小号栈空间 导致程序崩溃
无论函数是调用别的函数 还是调用自身 一定要做到快速收敛
在比较有限的次数内能够结束 而不是无限制的调用函数
官方的CPython默认情况下 调用栈的大小是1000

Author:25423
Date:2023/6/14
"""
import example04二分查找
import math
# 三方库
import requests

'''def main():
    print(math.factorial(5))
    resp = requests.get('https://www.sohu.com/index.html')
    print('resp.text')
    print(max(35, 343, 6556))'''


def foo():
    print('foo')


def bar():
    foo()
    print('bar')


def main():
    a,b=5,6
    bar()
    print(5,6)
    print('game over')

# main会调用到bar()
if __name__ == '__main__':
    main()
