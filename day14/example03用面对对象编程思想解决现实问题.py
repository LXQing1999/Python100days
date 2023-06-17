"""
example03用面对对象编程思想解决现实问题
计算游泳池的造价
Author:25423
Date:2023/6/16
"""
import math
class Circle:
    # 半径
    def __init__(self,radius):
        self.radius=radius
    # 周长
    def perimeter(self):
        return  2*math.pi*self.radius
    def area(self):
        return  math.pi*self.radius**2

if __name__ == '__main__':
    r=int(input('请输入游泳池半径:'))
    c1,c2=Circle(r),Circle(r+3)
    # 围墙造价,大圈周长
    fence_price=c2.perimeter()*38.5
    # 国道造价
    aisle_price=(c2.area()-c1.area())*88
    print(f'总计:{int(fence_price+aisle_price)}')
