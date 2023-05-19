"""
example08 随机抽样
Author:25423
Date:2023/5/19
"""
import random
fruits=['banana', 'dragon fruit', 'pineapple', 'strawberry', 'peach', 'cherry']
print(len(fruits))
# random.sample 不放回抽样，不会抽到重复的样本
print(random.sample(fruits,5))
# random.choices 放回抽样，可能会抽到重复的样本
print(random.choices(fruits,k=5))
# random.choice 默认只抽到一个元素
print(random.choice(fruits))
# random.shuffle 可以实现列表元素的随机乱序  音[ˈʃʌf(ə)l]
print(random.shuffle(fruits))