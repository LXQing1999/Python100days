"""
example08_获取json并解析

老师没有讲这个API怎么调用，我自己弄的显示  当前KEY未申请该API
修改下载三方库的下载来源为国内的镜像网站   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
三方库   pip install requests
使用http/https超文本传输协议访问网络资源的协议
Author:25423
Date:2023/6/4
"""
import requests

# s换行之后仍然是同一个字符串 两种写法都可以
'''
requests.get(
    'http://api.tianapi.com/guonei/index?'
    'key=78184a91b38fe4b579f281b87e551186&domain=www.baidu.com')
'''

resp=requests.get(
    url='http://api.tianapi.com/guonei/index',
    params={'key':'78184a91b38fe4b579f281b87e551186','domain':'www.baidu.com'}
)
'''
news_dict=resp.json()
news_list=news_dict['newslist']
for news in news_list:
    print(news['title'])
    print(news['url'])
'''