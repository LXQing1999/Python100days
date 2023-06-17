"""
example01面向对象编程
指令式编程->面向对象(函数)编程->程序比较简单的时候没有任何毛病
编程范式 （程序设计的方法论）：面向对象编程/函数式编程
对象:对象是可以接收消息的实体
对象=数据+函数(方法)   对象将数据和操作数据的方法从逻辑上变成了一个整体
类:将一大类对象共同的特征(静态特征和动态特征)抽取出来之后得到的一个抽象概念
简单的说,类是对象的模板,有了类才能够创建出这种类型的对象

面向对象编程
1.定义类 :命名要求首字母大写
    数据对象:找到和对象相关的静态特征(属性)
    行为对象:找到和对象相关的动态特征(方法    )
2.造对象
3.发消息
Author:25423
Date:2023/6/15
"""
# 定义类的关键字 class  首字母大写
class Student:
    # 定义函数  写到类里面的函数被称为方法
    # def __init__():这个是固定的格式
    # self代表这个学生对象
    # 数据抽象(属性)
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 行为抽象(方法)
    def eat(self):
        print(f'{self.name}正在吃饭')
    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')
    def play(self,game):
        print(f'{self.name}正在玩{game}')