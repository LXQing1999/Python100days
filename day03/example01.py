"""
example01
分支结构
代码中有多条执行路径，但是只有其中一条会被执行
Author:25423
Date:2023/5/4
"""
# import getpass
username = input('用户名： ')
password = input('密码： ')
# password = getpass.getpass('密码： ')
if (username == 'admin' and password == 'Admin123!!'):
    print('登录成功！')
    print('欢迎使用XX系统！')
else:
    print('登录失败！用户名或密码错误！')
print('程序执行结束！')
