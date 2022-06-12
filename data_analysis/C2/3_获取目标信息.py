#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 3_获取目标信息.py
@Auth: ciel7
@Date: 2022/6/12-下午5:49
@Desc: 
@Ver : 
"""
import requests
from bs4 import BeautifulSoup


def get_list(soup_list):
    """
    清洗解析后的网页信息，并以列表的形式返回
    :param soup_list: bs_list
    :return: lists
    """
    lists = []
    for ele in soup_list:
        lists.append(ele.string)
    return lists


# 访问网页、获取网页全部信息
url = "https://movie.douban.com/subject/1292064/"
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url=url, headers=headers)

# 获取目标信息
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# 存储容器，电影信息一览
movie_info = {}

# 电影名称 property="v:itemreviewed"
movie_info['title'] = soup.find(property="v:itemreviewed").text

# 简介部分
# 导演
movie_info['director'] = soup.find(rel="v:directedBy").text

# 编剧
movie_info['writer'] = soup.find_all(class_="attrs")[1].text

# 演员
movie_info['actors'] = get_list(soup.find_all(rel="v:starring"))

# 电影类型 property="v:genre"
movie_info['genre'] = get_list(soup.find_all(property="v:genre"))

# 遍历文档树 - https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id25
# .next_element 属性指向解析过程中下一个被解析的对象(字符串或tag),结果可能与 .next_sibling 相同,但通常是不一样的.
movie_info['language'] = soup.find(text="语言:").next_element

movie_info['release_date'] = soup.find(property="v:initialReleaseDate").string

movie_info['runtime'] = soup.find(property="v:runtime").text

# 评分部分
movie_info['average'] = soup.find(property="v:average").text
movie_info['votes'] = soup.find(property="v:votes").text

# print(movie_info)

for key in movie_info:
    # print(movie_info[key])
    print(key, ": ", movie_info.get(key))