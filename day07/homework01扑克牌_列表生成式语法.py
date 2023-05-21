"""
homework01 用一个列表保存54张扑克牌，先洗牌
再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第1个玩家（地主）
最后把每个玩家手上的牌显示出来
Author:25423
Date:2023/5/19
"""
import random
cards = []
Poker_suits = ['♠', '♥', '◆', '♣']
Card_count = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [f'{suite}:{count}' for suite in Poker_suits for count in Card_count]
cards.append('大王')
cards.append('小王')
print(f'洗牌前：{cards}')

# 随机乱序 random.shuffle() 洗牌
random.shuffle(cards)
print(f'洗牌后：{cards}')
'''
for Poker_suit in Poker_suits:
    for count in Card_count:
        print(f'{Poker_suit}:{count}')
        cards.append((f'{Poker_suit}{count}'))
'''
player1=[]
player2=[]
player3=[]

# 各分17张牌
for _ in range(17):
    # pop会删除card 还会返回card 所以可以用它append添加上
    player1.append(cards.pop())
    player2.append(cards.pop())
    player3.append(cards.pop())
# 剩下的牌都给player1
# player1.extend(cards)
player1+=cards

print(f'player1：{player1}')
print(f'player2：{player2}')
print(f'player3：{player3}')

player1.sort(key=lambda x:x[2:])
player2.sort(key=lambda x:x[2:])
player3.sort(key=lambda x:x[2:])

for card in player1:
    print(card,end=' ')
print()

print(f'排序后player1：{player1}')
print(f'排序后player2：{player2}')
print(f'排序后player3：{player3}')


