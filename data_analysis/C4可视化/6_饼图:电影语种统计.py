#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 6_饼图:电影语种统计.py
@Auth: ciel7
@Date: 2022/6/16-下午11:23
@Desc: 
@Ver : 
"""
import sys

sys.path.append('/Users/huxiaoting01/Coding/python/python-learning/data_analysis/')
import C3处理与分析.pandas_def as pdef
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pdef.language_tj()

print(data.head(1))

# 对数据进行排序
data = data.sort_values('tj', ascending=False)

# 绘制饼图
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

data = data[0:9]
# 类别数据
labels = data.index
sizes = data['tj'].tolist()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.title('电影语种统计')

plt.legend(title="language", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()