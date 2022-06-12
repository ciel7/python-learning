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


