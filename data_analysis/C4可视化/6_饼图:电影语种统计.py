#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 6_饼图:电影语种统计.py
@Auth: ciel7
@Date: 2022/6/16-下午11:23
@Desc: 如何理解散点图：相关性，是否存在趋势？不同区域隐含的信息
@Ver : 
"""
import sys

sys.path.append('/Users/huxiaoting01/Coding/python/python-learning/data_analysis/')
import C3处理与分析.pandas_def as pdef
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

data = pdef.average_votes()

print(data.head(1))

plt.scatter(x=data['average'], y=data['votes'])
title = len(data).__str__() + " 部电影评分分值与人数"
plt.title(title)
plt.xlabel('评分分值')
plt.ylabel('评价人数')
plt.grid()

plt.show()

# 筛选、排序 --> 结合图表，观察数据
print("-------------  高分热门电影  --------------------")
print(data.sort_values(['votes', 'average'], ascending=False).head(20))