#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 1_Requests入门.py
@Auth: huxiaoting01@baidu.com
@Date: 2022/6/11-下午5:20
@Desc: 
@Ver : 
"""

# 导入模块
import requests

# 定义 Url
url_douban_movie = "https://movie.douban.com"

# headers
headers = {'user-agent': 'my-app/0.0.1'}

# 访问、并获取网页信息
response_douban_movie = requests.get(url=url_douban_movie, headers=headers)
# print(response_douban_movie.text)

# 千与千寻电影主页
url2 = "https://movie.douban.com/subject/1291561/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia"
response2 = requests.get(url=url2, headers=headers)
# print(response2.text)

# 百度百科主页
url3 = "https://baike.baidu.com"
response3 = requests.get(url=url3, headers=headers)
print(response3.text)
