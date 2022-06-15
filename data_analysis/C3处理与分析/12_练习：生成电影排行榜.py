#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 12_练习：生成电影排行榜.py
@Auth: ciel7
@Date: 2022/6/15-下午9:14
@Desc: 
@Ver : 
"""

# 获取数据
import pandas as pd
import numpy as np

# 显示所有列（参数设置为 None 代表显示所有行，也可以自行设置数字）
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为 50
pd.set_option('max_colwidth', 10)

# 获取清洗后的电影数据
data = pd.read_csv('../data/movie_data_cleaned.csv')
# print(data)

# 筛选分值>80w
data = data[data['votes'] > 800000]

# 针对评分分值、评价人数进行排序（逆序）
data_sorted = data.sort_values(by=['average', 'votes'], ascending=False)
data_sorted = data_sorted[['title', 'average', 'votes']]
print(data_sorted.head(250))

# 提取位于前 250 位的电影数据
# data_sorted.iloc[0:249]
data_sorted.head(250)