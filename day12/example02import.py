"""
example02  导入函数
import函数 as 重命名
解决命名冲突问题
Author:25423
Date:2023/6/13
"""
import utils.bar
import random
# 别名
from utils.static import median as med

data = [random.randrange(1, 101) for _ in range(8)]
print(med(data))
# 完全限定名
print(utils.bar.average(data))


























