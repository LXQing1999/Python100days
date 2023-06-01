"""
example05 
Author:25423
Date:2023/6/1
"""
import string
# string.ascii_lowercase包含所有小写字母的字符串
# 创建了一个名为 results 的字典，其中每个字母都对应着一个初始值为 0 的计数器
results={letter:0 for letter in string.ascii_lowercase}
# 提示用户输入一个字符串，并将其转换为小写字母形式。
content=input('请输入：').lower()

for char in content:
    if char in results:
        results[char]+=1
print(results)

for key,value in results.items():
    # :>2d chatgpt坏了，还需要进一步了解
    print(f'{key}:{value:>2d}次')