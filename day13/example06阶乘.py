"""
example06阶乘 
Author:25423
Date:2023/6/15
"""
def fac(num:int)->int:
    if num==0:
        return 1
    return num*fac(num-1)
if __name__ == '__main__':
    for i in range(10):
        print(i,fac(i))