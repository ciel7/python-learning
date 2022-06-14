#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 6_数据运算：类型统计.py
@Auth: ciel7
@Date: 2022/6/14-下午7:43
@Desc: 
@Ver : 
"""

import pandas as pd
import numpy as np

# 显示所有列（参数设置为None代表显示所有行，也可以自行设置数字）
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为 50
pd.set_option('max_colwidth', 30)

# 读取数据
data = pd.read_csv('../data/movie_data_cleaned.csv')

# 获取所有类型：提取每一行的 genre 元素 --> 新的列表 genre_list ---> 去重

data['genre'] = data['genre'].str.strip('[')
data['genre'] = data['genre'].str.strip(']')
data['genre'] = data['genre'].fillna(value='')

genre_list = []
for g in data['genre']:
    g_list = g.split(', ')

    for label in g_list:
        genre_list.append(label)

genre_list = list(set(genre_list))
genre_list.remove('')
# print(genre_list)

# 2列：标签，统计值 tj -----> '剧情'    0.0
data_genre_tj = pd.DataFrame(np.zeros([len(genre_list), 1]), index=genre_list, columns=['tj'])

for i in data['genre']:
    for label in genre_list:
        if str(i).__contains__(label):
            data_genre_tj.loc[label, 'tj'] += 1

print(data_genre_tj)
