#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 4_折线图：各国电影年产量.py
@Auth: ciel7
@Date: 2022/6/16-下午8:17
@Desc: 
@Ver : 
"""
import sys

sys.path.append('/Users/huxiaoting01/Coding/python/python-learning/data_analysis/')
import C3处理与分析.pandas_def as pdef
import matplotlib.pyplot as plt
import numpy as np

data = pdef.country_year_tj()

print(data.head(1))

# 中文乱码
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 绘制折线图
data.plot()
plt.legend(ncol=4)
plt.title('各国电影年产量')
plt.xlabel('年份')
plt.ylabel('数量')
plt.show()
