"""
exameple03    百钱百鸡问题    穷举法
公鸡五块，母鸡3块，三只小鸡1块，一共一百块,要买一百只鸡，问能买各多少只鸡
Author:25423
Date:2023/5/7
"""
for i in range(1, 21):
    for j in range(0, 34):
        k = 100 - i - j
        if 5 * i + 3 * j + k // 3 == 100:
            print(i, j, k)
'''
for i in range(1,21):
    for j in range(0,34):
        for k in range(0,100,3):
            if i+j+k ==100  and 5*i+3*j+k//3 <=100  :
                print(i,j,k)
'''
