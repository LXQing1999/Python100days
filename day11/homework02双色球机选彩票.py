"""
homework02双色球机选彩票
选择不重复的6个球，从小到大排序
蓝色球一个，跟在红球的后面

注意print时，不同的格式化输出规则
Author:25423
Date:2023/6/5
"""
import random
n=int (input('机选几注：'))
for _ in range(n):
# 列表的生成式语法
    red_ball=[i for i in range(1,34)]
    blue_ball=[i for i in range(1,17)]
# random.sample随机抽样
    selected_balls=random.sample(red_ball,6)
    selected_balls.sort()
    # selected_balls.append(random.choice(blue_ball,k=1))
    selected_balls+=random.choices(blue_ball,k=1)
    print(selected_balls)
    # 遍历selected_balls中除了最后一个元素之外的所有元素;
    # 变量ball会被替换为一个0填充的两位数
    for ball in selected_balls[:-1]:
        print(f'{ball:0>2d}',end=' ')
    # 输出一个格式化的字符串，其中的变量selected_balls[-1]会被替换为selected_balls中的最后一个元素，
    # 在最后一个元素之前，会打印一个竖线符号（|）
        print(f'|{selected_balls[-1]:0>2d}')

