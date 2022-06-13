#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 4_连续获取多个页面信息.py
@Auth: ciel7
@Date: 2022/6/12-下午6:50
@Desc: 访问豆瓣 top250 主页，跳转下一页，实现每个页面信息的抓取
@Ver : 
"""

import requests
from bs4 import BeautifulSoup

# 访问 TOP250 主页
# 访问网页、获取信息
headers = {'user-agent': 'my-app/0.0.1'}

# 跳转页面（https://movie.douban.com/top250?start=0&filter=）
page = 0
size = 25
max_page = 225  # start 参数对应的值

responses = {}
movie_links = []
movie_names = []
while page <= max_page:
    # 组织 url
    # url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="
    url = "https://movie.douban.com/top250?start=" + page.__str__() + "&filter="
    # print(url)
    # 访问页面
    response = requests.get(url=url, headers=headers)
    # print(response.text)

    # 访问每个页面，实现电影单链信息的获取
    soup = BeautifulSoup(response.text, 'html.parser')

    for ele in soup.find_all(class_="hd"):
        movie_names.append(ele.find(class_="title").text)
        movie_links.append(ele.find('a', href=True).attrs['href'])

    # 修改 start 参数
    page += size

# 浏览所有抓取到的信息
for name, link in zip(movie_names, movie_links):
    print(name, ":", link)
