"""
example05三角形
描述三角形的类 计算三角形的周长和面积
我们在类里面写的函数,通常称之为方法 它们基本上都是发给对象的消息
但是有的时候 我们的消息不是想发给对象 而是希望发给这个类(类本身也是一个对象)
此时  我们可以使用静态方法或类方法
静态方法 发给类的消息  @staticmethod  装饰器
类方法 发给类的方法     @staticmethod   装饰器   第一个参数是接收消息的类

通过构造器语法创建的对象基本都在堆空间
而对象的引用通常是放在栈上的 通过引用就可以访问到对象并向其发出消息
Author:25423
Date:2023/6/17
"""

class Triangle:
    def __init__(self, a, b, c):
        if not Triangle.is_valid(a,b,c):
            # raise是关键字 专门用来引发异常的
            raise ValueError('无效的边长,无法构成三角形')
        self.a = a
        self.b = b
        self.c = c
    # @classmethod
    # def is_valid(cls,a,b,c):
        # return a+b>c and a+c>b and b+c>a
    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and a+c>b and b+c>a

    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        # 海伦公式
        half=self.perimeter()/2
        return 0.5**((half-self.a)*(half-self.b)*(half-self.c))
'''     if a+b>c and a+c>b and b+c>a:
            self.a = a
            self.b = b
            self.c = c
        else:
            # raise是关键字 专门用来引发异常的
            raise ValueError('无效边长,无法构成三角形')'''

# 如果try中的代码没有发生异常 或者发生了异常 但是except没有捕获到 就不不会执行except里面的代码

if __name__ == '__main__':
    # if Triangle.is_valid()
    try:
        t=Triangle(3,2,1)
        print(t.perimeter())
        print(t.area())
    except ValueError as err:
        print(err)