# !/usr/bin/env python
# encoding: utf-8
"""
@Name: 9_练习：计算电影数据相关统计.py
@Auth: ciel7
@Date: 2022/6/15-上午9:39
@Desc: 
@Ver : 
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 10)

data = pd.read_csv('../data/movie_data_cleaned.csv',
                   usecols=['title', 'country', 'language', 'release_date', 'average'])

# 调整列标签的顺序
data = data[['title', 'country', 'language', 'release_date', 'average']]
# print(data)

# 各国每年的电影产量
'''
中国
1990 100
1991 200
1、明确国家类别数据：有多少个富哦家 --> country_list
2、筛选每个国家，并定义为一个 dataframe
3、针对每个国家df，使用resample.count()统计每个国家的年产量
'''
data['country'] = data['country'].str.strip(' ')
data['country'] = data['country'].fillna(value='')

country_list = []
for c in data['country']:
    c_list = c.split('/')
    for label in c_list:
        label = label.strip(' ')
        country_list.append(label)

country_list = list(set(country_list))
country_list.remove('')
print(country_list)

# print(data[data['country'].str.contains('中国')])


data['release_date'] = pd.to_datetime(data['release_date'])
data = data.set_index(data['release_date'])


for label in country_list:
    temp = data[data['country'].str.contains(label)]

    country_year_tj = temp['release_date'].resample('Y').count()

    print(label, country_year_tj)