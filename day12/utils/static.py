"""
homework04样本数据描述性信息
集中趋势:均值 中位数 众数
离散趋势:极差 方差 标准差
Author:25423
Date:2023/6/13
"""
# data可以是一个列表
# 集合 ,它要是一个可迭代对象
# 实际上Python是一个很易学的语言,即使没有明确标出是float也不会像c++一样报错
import math
import random


# 求极差
def ptp(data) -> float:
    return max(data) - min(data)


# 求均值
def average(data):
    return sum(data) / len(data)


# 求方差
# 无偏估计 分母为什么是n-1   https://www.matongxue.com/madocs/607/
def variance(data):
    aver = average(data)
    total = 0
    for i in data:
        total += (i - aver) ** 2
    return total / (len(data) - 1)


# 求标准
# 差
def standrd_deviastion(data):
    return math.sqrt(variance(data))


# 减少工作量,尽量不要给data.sort()以免影响原来的data数组
# sorted(data)不会改变原本的数据 只会返回一组暂时的新数据
# len(data)//2是整除,相当于只保留前面的整数部分
def median(data):
    temp = sorted(data)
    if (len(temp) % 2 == 1):
        return temp[len(data) // 2]
    else:
        return average(temp[len(data) // 2 - 1:len(data) // 2 + 1])

print(__name__)
#  __name__是隐藏变量 代表当前
#  模块的名字 ,如果未指定的话 默认是 dominate main
#吧如果是在其他文件中导入了homework04  那么此时的__name__就是homework04
# 这是为了保证,只有执行本函数时,才会政策输出  如果是被调用的 就不用输出
if __name__ == '__main__':
    nums = [random.randrange(1, 101) for _ in range(8)]
    print(nums)
    print(f'平均值:{average(nums)}')
    print(f'中位值:{median(nums)}')
    print(f'极差:{ptp(nums)}')
    print(f'方差:{variance(nums)}')
    print(f'标准差:{standrd_deviastion(nums)}')

