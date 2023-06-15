
# 只要路径正确,就算更改源也可以正常运行
# 如果没有特别写,那就是默认本文件夹中的源
import random
# from homework04样本数据描述性信息 import average ,median
from utils.static import  average ,median


'''def average(data):
    return sum(data) / len(data)'''
# random.randrange(60,101)范围是左闭右开的
A_scores=[random.randrange(60,101) for _ in range(50)]
B_scores=[random.randrange(60,101) for _ in range(50)]


print(A_scores)
print(f'平均分:{average(A_scores)}')
print(f'中位数:{median(A_scores)}')
print(B_scores)
print(f'平均分:{average(B_scores)}')
print(f'中位数:{median(B_scores)}')
