"""
homework02大乐透机选彩票
不太懂这些彩票怎么玩的，反正讲了 传参数

Author:25423
Date:2023/6/5
"""
import random
# 列表的生成式语法

def generate(red_ball_max, red_ball_num, blue_ball_max, blue_ball_num):
    '''生成一组号码
    return保存一组彩票号码的列表'''
    global selected_balls
    red_ball = [i for i in range(1, red_ball_max + 1)]
    blue_ball = [i for i in range(1, blue_ball_max + 1)]
    # 随机抽取几个球
    selected_red_balls = random.sample(red_ball, blue_ball_num)
    selected_red_balls.sort()
    # selected_balls.append(random.choice(blue_ball,k=1))
    selected_blue_balls = random.choices(blue_ball, k=2)
    selected_blue_balls.sort()

    return selected_red_balls + selected_blue_balls


def display(balls):
    '''显示一组彩票号码
balls 装彩票号码的球的列表
    '''
    for ball in balls:
        print(f'{ball:0>2d}', end=' ')
    print()


n = int(input('机选几注：'))
print('双色球：')
for _ in range(n):
    display(generate(33,6,16,1))
print('大乐透：')
for _ in range(n):
    display(generate(35, 5, 12, 2))