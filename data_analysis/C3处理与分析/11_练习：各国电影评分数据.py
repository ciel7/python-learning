#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 11_练习：各国电影评分数据.py
@Auth: ciel7
@Date: 2022/6/15-下午8:17
@Desc: 
@Ver : 
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 10)

# 获取数据
data = pd.read_csv('../data/movie_data_cleaned.csv', usecols=['title', 'country', 'average'])

data = data[['title', 'country', 'average']]

# 国家类别数据
data['country'] = data['country'].str.strip(' ')
data['country'] = data['country'].fillna(value='')

country_list = []

for c in data['country']:
    c_list = c.split('/')

    for label in c_list:
        country_list.append(label)

country_list = list(set(country_list))
country_list.remove('')

# 获取各评分类别数据
x = 2.2
rate_list = []
while x < 10.0:
    rate_list.append(x)
    x += 0.1
    x = x.__round__(1)

data_rate_tj = pd.DataFrame(np.zeros([len(rate_list), 1]), index=rate_list, columns=['tj'])
# 根据国家标签筛选 df
for country in country_list:
    # 生成各国 df 数据
    temp = data[data['country'].str.contains(country)]
    data_rate_tj[country] = 0.0
    # 遍历各国df内评分值得数据
    for r in temp['average']:
        for label in rate_list:
            if r == label:
                data_rate_tj.loc[label, country] += 1

    print("国家：", country)
    print(data_rate_tj)

# 整合数据
