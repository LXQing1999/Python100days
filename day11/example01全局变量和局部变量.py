"""
example01
全局变量：没有写在任何函数的里面
局部变量：定义在函数内部
python 程序中搜索一个变量是安装LEGB顺序进行搜索的
Local 局部作用域
Emable
Author:25423
Date:2023/6/6
"""
x=100
def foo():
    # 里面的是局部变量
    x=200
    print(x)
    def bar():
        x=300
        print(x)
# 这个输出的是全局变量
foo()
print(x)