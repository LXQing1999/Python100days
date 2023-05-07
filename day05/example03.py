"""
example03 列表的遍历（把每个元素依次取出）
Author:25423
Date:2023/5/7
"""
# Python中对数组元素的类型要求没有那么严格
nums = [35, 9.8, 'hello', '热爱', 66]
print(nums[0], nums[-5])  # python中还可以使用负数
print(nums[1],nums[-3])  # 负数是从右往左数的，最右边是负一
print(nums[4],nums[-1])
nums[2] = 120
print(nums)

# 使用enumerate枚举，可以用来罗列序号
for i,x in enumerate(nums):
    print(i,x)


# 在Python里甚至遍历指针都这么简单？
# 众所周知，数组名是指针，居然可以直接用For来遍历！
for j in nums:
    print (j)
print('='*20)  # 这就是打印20遍Hello，太牛啦
for i in range(len(nums)):
    print(nums[i])  # 遍历数组
    nums[i]=100
print(nums[i])
# 负向遍历也能用，但是花里胡哨不推荐
for i in range(-5, 0):
    print(nums[i])  # 遍历数组
