"""
example03跑马灯文字效果
清楚屏幕输出：Windows cls  MAC_OS clear
Author:25423
Date:2023/5/22
"""
import time
import os
name= 'LXQing'

# 需要用到终端来运行
while True:
    os.system('cls')  # 清屏
    print(name)
    time.sleep(0.5)  # 休眠
    name= name[1:] + name[0]


'''
content2='XQing    L'
content3='Qing    LX'
content3='ing    LXQ'  
'''
