"""
homework01嵌套列表
用一个列表保存54张扑克牌，先洗牌
再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第1个玩家（地主）
最后把每个玩家手上的牌显示出来
Author:25423
Date:2023/5/20
"""
import random
cards = []
Poker_suits = ['♠', '♥', '◆', '♣']
Card_count = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# 列表生成式语法（推导式）
cards = [f'{suite}:{count}' for suite in Poker_suits for count in Card_count]
# 向列表上追加元素
cards.append('大王')
cards.append('小王')
print(f'洗牌前：{cards}')

# 随机乱序 random.shuffle() 洗牌
random.shuffle(cards)
print(f'洗牌后：{cards}')

# 嵌套列表 列表中的元素又是列表
players=[[] for _ in range(3)]

for _ in range(17):
    for player in players:
# 数组用pop删除最后一个元素比较合适，因为删除前面的，所有的元素都要动，比较费时
        player.append(cards.pop())

# 合并列表元素
# extend本意是延伸、延展，在这里是八剩下的牌都给player[0]
players[0].extend(cards)
# players[0]+=cards

for player in players:
    # sort 对列表中的元素进行排序
    player.sort(key=lambda x:x[1:])
    for card in player:
        print(card, end=' ')
    print()
