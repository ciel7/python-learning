#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 2_BeautifulSoup.py
@Auth: huxiaoting01@baidu.com
@Date: 2022/6/11-下午6:50
@Desc: 
@Ver : 
"""
import requests
from bs4 import BeautifulSoup

# 获取网页全部信息
url = "https://movie.douban.com/subject/1292064/"
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url=url, headers=headers)
# print(response.text)

print("\n ----------------------------------- \n")
# 解析网页信息
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

# 提取目标信息
# title = soup.title.text
# 楚门的世界 (豆瓣)
title = soup.title.string
print(title)

# find_all() 搜索当前 tag 的所有子节点，并判断是否符合过滤器的条件。
# name = soup.find_all(property="v:summary")
# 看报错信息，这是个list
# summary = soup.find_all(property="v:summary").string
summary = soup.find_all(property="v:summary")[0].text
print(summary)