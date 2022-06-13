#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 7_按标签获取电影数据.py
@Auth: ciel7
@Date: 2022/6/13-下午2:26
@Desc: 
@Ver : 
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'
headers = {'user-agent': 'my-app/0.0.1'}
movie_lists = []
movie_links = []
movie_names = []
all_infos = []


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


# 1.访问主页面，并且完成页面的跳转
def get_page(page_link, tags, genres):
    page = 0
    size = 20
    max_page = 100  # start 参数对应的值

    while page <= max_page:
        url = page_link + "?start=" + page.__str__() + "&tags=" + tags + "&genres=" + genres

        print(url)
        response = requests.get(url=url, headers=headers)
        movie_info = response.text

        print(movie_info)
        exit()
        # 将获取到的 string 转为字典, eval() === dict()
        movie_info = eval(movie_info)

        # 将字典里的数据，转储到列表中
        for m in movie_info['data']:
            # m 是字典类型的数据
            movie_lists.append(m)
            # 处理 url，将 \/ 替换为 /
            url_str= m.get('url')
            url_str.replace('\/', '/')
            movie_links.append(m.get('url'))

        # 修改 start 参数
        page += size

        print(url)



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


# 模拟登录，爬取次数多，被限制了
def login():
    get_url = 'https://www.douban.com/people/258010830/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
    }
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'remember': 'true',
        'username': '15503643123',
        'password': 'Hunan19970708.'
    }
    session = requests.Session()
    resopnse = session.post(url, headers=header, data=data)
    new_response = session.get(get_url, headers=header)
    if new_response.status_code == 200:
        with open('new-html.html', 'wb')as f:
            f.write(new_response.content)
            f.close()
    else:
        print('登录错误')

if __name__ == '__main__':
    login()
    exit()
    # 1. 调用 get_page 实现页面的访问
    get_page(page_link="https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=", tags="电影", genres="动画")

    # 调用获取详细信息的方法
    for link in movie_links:
        print("正在抓取电影：", link)
        get_infos(url=link)
    # 拿到电影信息，list.append存储容器，list > dataFrame > to_excel()
    data = pd.DataFrame(movie_lists)
    data.to_excel("豆瓣动画电影.xlsx")