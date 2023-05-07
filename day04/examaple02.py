"""
examaple07   输出乘法口诀表
Author:25423
Date:2023/5/6

\t ：表示空4个字符，类似于文档中的缩进功能，相当于按一个Tab键。
\n ：表示换行，相当于按一个 回车键
\n\t : 表示换行的同时空4个字符。
"""

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end=' ')
    print()   # 输出默认的换行
