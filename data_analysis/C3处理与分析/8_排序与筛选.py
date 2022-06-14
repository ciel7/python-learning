#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 8_排序与筛选.py
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

data = pd.read_csv('../data/movie_data_cleaned.csv')

# 对列标签进行排序，单列/多列，正序/逆序
# data.sort_values('title', ascending=True)
# print(data[['average', 'votes']].sort_values(['average', 'votes'], ascending=False))

# 筛选：行（索引、值、行数）、列、行列
# print(data.iloc[0:100])
# print(data.loc[data['average'] == 9.7])
print(data[['title', 'genre']])
# 满足行列双重条件
print(data.loc[data['average'] == 9.7, ['title', 'genre']])

# 评分最高前5
print(data[['title', 'average', 'votes']].sort_values('average', ascending=False).head(5))

# 评价人数最多前5
print(data[['title', 'average', 'votes']].sort_values('votes', ascending=False).head(5))

# 两者兼具前10
print(data[['title', 'average', 'votes']].sort_values(['average', 'votes'], ascending=False).head(10))

