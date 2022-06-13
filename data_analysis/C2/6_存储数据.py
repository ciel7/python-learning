#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 5_整合爬虫功能函数.py
@Auth: ciel7
@Date: 2022/6/13-上午11:17
@Desc: 
@Ver : 
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

movie_links = []
movie_names = []
all_infos = []
headers = {'user-agent': 'my-app/0.0.1'}


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


# 1.访问主页面，并且完成页面的跳转，跳转页面（https://movie.douban.com/top250?start=0&filter=）
def get_page(page_link):
    page = 0
    size = 25
    max_page = 225  # start 参数对应的值

    while page <= max_page:
        # 组织 url
        # url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="
        url = page_link + "?start=" + page.__str__() + "&filter="
        response = requests.get(url=url, headers=headers)
        get_links(response)
        # 修改 start 参数
        page += size


# 2.抓取每个页面所有的电影链接
def get_links(response):
    # 访问每个页面，实现电影单链信息的获取
    soup = BeautifulSoup(response.text, 'html.parser')

    for ele in soup.find_all(class_="hd"):
        movie_names.append(ele.find(class_="title").text)
        movie_links.append(ele.find('a', href=True).attrs['href'])


# 3.根据电影链接，获取电影基本信息、评分信息
def get_infos(url):
    # 访问网页、获取网页全部信息
    response = requests.get(url=url, headers=headers)

    # 获取目标信息
    soup = BeautifulSoup(response.text, 'html.parser')

    # 存储容器，电影信息一览
    movie_info = {}

    # 容错处理
    try:
        # 电影名称 property="v:itemreviewed"
        movie_info['title'] = soup.find(property="v:itemreviewed").text

        # 简介部分
        # 导演
        movie_info['director'] = soup.find(rel="v:directedBy").text

        # 编剧
        writer = soup.find_all(class_="attrs")
        # 相比 5_整合爬虫功能函数.py 有代码优化
        # if len(writer) > 1:
        #     movie_info['writer'] = soup.find_all(class_="attrs")[1].text
        # else:
        #     movie_info['writer'] = ""
        # print(writer)
        # print(len(writer))
        # print(get_list(soup.find_all(class_="attrs")[1].find_all('a')))
        if len(writer) > 1:
            movie_info['writer'] = get_list(soup.find_all(class_="attrs")[1].find_all('a'))
        else:
            movie_info['writer'] = ""

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
        movie_info['link'] = url

        # 打印电影信息
        for key in movie_info:
            # print(movie_info[key])
            print(key, ": ", movie_info.get(key))
    except AttributeError:
        print("电影已下架")

    # 电影信息存到列表中
    all_infos.append(movie_info)


if __name__ == '__main__':
    # 1. 调用 get_page 实现页面的访问
    get_page(page_link="https://movie.douban.com/top250")

    # 获取每个页面信息 ---> 调用获取页面所有电影链接 ---> for 循环，调用获取信息的功能
    for name, link in zip(movie_names, movie_links):
        get_infos(link)

    # 将电影信息转为二维表，并存到电子表格中
    data = pd.DataFrame(all_infos)
    data.to_excel("豆瓣250部高分电影.xlsx")
