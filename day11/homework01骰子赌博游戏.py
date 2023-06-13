"""
homework01骰子游戏
赌博要不得，就算从1000块摇到了7035，多来几次同样会亏光本金

玩家摇两颗骰子，如果第一次摇出了7或11点。玩家胜，如果摇出了2点，3点，11点，庄家胜
如果摇出其他点数，游戏继续，玩家重新摇骰子；如果玩家摇出第一次摇的点数，玩家胜；
如果玩家摇出了7点，庄家胜，如果玩家摇出了其他点数，游戏继续，玩家重新摇骰子，直到分出胜负

游戏开始之前，玩家有1000元的初始资金，玩家可以下注，赢了获得下注的金额，输了就扣除下注的金额
游戏结束的条件是玩家把钱输光。

# 技巧：选中按tab向右空格，shift+tab取消缩进
try:
    # 可能会发生异常的代码
except [ExceptionType]:
    # 异常处理代码
如果[ExceptionType]没有指定，，则会捕捉所有类型的异常。

将函数封装，实现函数的复用
Author:25423
Date:2023/6/5
"""

import random
# 传入自变量，返回因变量

money=1000
while money>0:
    print(f'玩家资产{money}元')
    mark=0
# 处理异常的代码try except
    while mark<=0 or mark>money:
        try:
            mark=int(input('请下注：'))
        except ValueError:
            print('无效输入')
            pass
    first_point=random.randrange(1,7)+random.randrange(1,7)
    print(f'玩家首次摇出了{first_point}点')
    '''
    if(first_point==7 or first_point==11):
        print('玩家胜！')
    '''
    # 换一种写法，如果点数，在这个二元组中
    if first_point in(7,11):
        print('玩家胜！')
        money+=mark
    elif first_point in (2,3,12):
        print('庄家胜！')
        money -= mark
    else:
        # 摇出点数均不符合元组元素
        while True:
            # 重新摇骰子
            curr_point=random.randrange(1,7)+random.randrange(1,7)
            print(f'玩家摇出了{curr_point}点')
            if(curr_point==first_point):
                print('玩家胜！')
                money += mark
                break
            elif curr_point==7:
                print('庄家胜！')
                money -= mark
                break
