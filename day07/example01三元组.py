"""
example01 保存五个学生，三门课程的成绩

Author:25423
Date:2023/5/20
"""
import random

names = ['Sam', 'Jhon', '张三', '李四', '王五', '赵六']
courses = ['语文', '数学', '外语']
scores = [[random.randrange(60, 100) for _ in range(len(courses))]
          for _ in range(len(names))]
print(scores)
'''
# 三元组   scores[i][j] 行列
scores = [[90, 85, 64], [74, 78, 65], [87, 94, 64], [74, 65, 83], [96, 95, 67]]
names=['Sam','Jhon','张三','李四','王五']
courses=['语文','数学','外语']
'''
# 每个学生的各科目成绩
for i, name in enumerate(names):
    for j, course in enumerate(courses):
        print(f'{name}的{course}成绩：{scores[i][j]}')
# 统计每个学生的平均成绩
for i, name in enumerate(names):
    average = sum(scores[i]) / len(courses)
    print(f'{name}的平均成绩：{average:.1f}')

# 统计每门课的最高分和最低分
for j, course in enumerate(courses):
    # 创建了一个临时列表temp，用于存储当前课程所有学生的成绩
    temp = [scores[i][j] for i in range(len(names))]
    print(temp)
    # max(temp)居然可以直接把数组名放进去进行max运算
    print(f'{course}的最高分：{max(temp)}')
    print(f'{course}的最高分：{min(temp)}')
