"""
homework01骰子游戏
将函数封装，实现函数的复用,类似C语言中的结构体
自变量argument ->参数parameter
因变量 ->返回值return value

自定义函数的时候，最好写上文档注释
Author:25423
Date:2023/6/5
"""

import random
'''
摇骰子
param(参数) num骰子数量
return 摇出的点数
'''
def roll_point(num):
    total=0
    for _ in range(num):
        total+=random.randrange(1, 7)
    return total

# 传入自变量，返回因变量
'''
def roll_point():
    point = random.randrange(1, 7) + random.randrange(1, 7)
    return point
'''
money = 1000
def pleyer_win(money):
    print('玩家胜！')
    money += mark
    return money

def holder_win(money):
    print('庄家胜！')
    money -= mark
    return money

while money > 0:
    print(f'玩家资产{money}元')
    mark = 0
    # 处理异常的代码try except
    while mark <= 0 or mark > money:
        try:
            mark = int(input('请下注：'))
        except ValueError:
            print('无效输入')
            pass
    # first_point = roll_point()
    first_point = roll_point(2)
    print(f'玩家首次摇出了{first_point}点')

    if first_point in (7, 11):
        pleyer_win(money)
    elif first_point in (2, 3, 12):
        holder_win(money)
    else:
        # 摇出点数均不符合元组元素
        while True:
            # 重新摇骰子
            curr_point = roll_point(2)
            print(f'玩家摇出了{curr_point}点')
            if (curr_point == first_point):
                pleyer_win(money)
                break
            elif curr_point == 7:
                holder_win(money)
                break
