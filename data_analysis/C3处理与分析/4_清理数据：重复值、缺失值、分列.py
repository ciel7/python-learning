#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 4_清理数据：重复值、缺失值、分列.py
@Auth: ciel7
@Date: 2022/6/13-下午10:34
@Desc: 
@Ver : 
"""

import pandas as pd

# 显示所有列（参数设置为None代表显示所有行，也可以自行设置数字）
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为 50
pd.set_option('max_colwidth', 30)

data = pd.read_csv("../data/movie_data.csv", usecols=['average', 'genre', 'country', 'language', 'release_date', 'title', 'votes'])
# print(data)

# 根据title：查重、去重
# 识别是否重复，返回 true、false
duplicate_df = data.duplicated('title')
# 根据指定列名称，删除重复数据
duplicate_data = data.drop_duplicates('title')

# 缺失值：NaN，评分/人数 ---> 为空的填充平均值，文本数据 ---> NaN
nan_df = pd.isna(duplicate_data)
# print(nan_df)
# 平均值
# print(duplicate_data['average'].mean())
duplicate_data['average'] = round(duplicate_data['average'].fillna(value=duplicate_data['average'].mean()), 2)
duplicate_data['votes'] = round(duplicate_data['votes'].fillna(value=duplicate_data['votes'].mean()), 0)

# duplicate_data[''] = duplicate_data['average'].fillna(value=duplicate_data['average'].mean())
# 分列
# 10437 [1997-04-02, 美国)]
# print(duplicate_data['release_date'].str.split('(', expand=False))
# 10437  1997-04-02 美国)
duplicate_data['release_date'] = duplicate_data['release_date'].str.split('(', expand=True)[0]

# 预览清洗后的数据
print(duplicate_data)

duplicate_data.to_csv('../data/movie_data_cleaned.csv')
print("已完成数据清洗，并保存至movie_data_cleaned，数据条数：", len(duplicate_data))