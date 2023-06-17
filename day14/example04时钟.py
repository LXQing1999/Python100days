"""
example04时钟
名词:
    `时钟:类
    `属性:时分秒
动词:显示 走字

Author:25423
Date:2023/6/16
"""
import os
import time
class Clock:
    # 名词  *后面的是命名关键字参数
    def __init__(self,*,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    # 动词
    def show(self):
        # 显示     用0补齐两位的位置
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'

    def run(self):
        self.second+=1
        if self.second==60:
            self.second=0
            self.minute+=1
            if self.minute==60 :
                self.minute=0
                self.hour+=1
                if self.hour==24:
                    self.hour=0

if __name__ == '__main__':
    clock=Clock()
    while True:
        os.system('cls')
        print(clock.show())
        time.sleep(1)
        clock.run()