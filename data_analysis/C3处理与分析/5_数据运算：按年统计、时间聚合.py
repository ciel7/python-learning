#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 5_数据运算：按年统计、时间聚合.py
@Auth: ciel7
@Date: 2022/6/14-下午7:43
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

# 读取数据
data = pd.read_csv('../data/movie_data_cleaned.csv')

# 读取日期
print(data.head(3)['release_date'])

# 对于年份进行统计：1900-2000
# resample（时间间隔参数：年、季度、月、周）.count()/cum()/asfreq()
# 替换索引（Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex）
data['release_date'] = pd.to_datetime(data['release_date'])
data = data.set_index(data['release_date'])
data_year_tj = data['release_date'].resample('Y').count()

# 打印统计数据
print(data_year_tj.head(3))

