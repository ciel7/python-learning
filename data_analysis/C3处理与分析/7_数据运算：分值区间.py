#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 7_数据运算：分值区间.py
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

# 1、知道当前数据区间：最大值、最小值
print(data['average'].describe())

# 2、获取个评分类别数据
rate_list = []

# 根据 data['average'].describe() 了解到最小值为：2.2
x = 2.2
while x <= 10.0:
    rate_list.append(x)
    x += 0.1
    x = x.__round__(1)

# print(rate_list)

# 依次进行统计：for 每一行、单元格，判断数据 = label，rate统计df对应的tj+1
data_rate_tj = pd.DataFrame(np.zeros([len(rate_list), 1]), index=rate_list, columns=['tj'])

for r in data['average']:
    for label in rate_list:
        if r == label:
            data_rate_tj.loc[label, 'tj'] += 1

print(data_rate_tj)