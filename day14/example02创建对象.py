"""
example02创建对象 
Author:25423
Date:2023/6/16
"""
from example01面向对象编程 import Student
# 第二步:创建对象->构造器语法->类名
# 注意类的首字母要求大写
stu1=Student('张三',15)
stu2=Student('李四',18)

# 重新赋值
stu1.name='王五'

Student.play(stu1,'王者')
# 第三步:给对象发消息(调用对象的方法)
stu2.play('扫雷')
