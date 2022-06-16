#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 3_直方图：电影年产量.py
@Auth: ciel7
@Date: 2022/6/16-上午9:28
@Desc: 电影年产量：电影数量呈上升趋势，电影行业逐渐繁荣
@Ver : 
"""
import sys

sys.path.append('/Users/huxiaoting01/Coding/python/python-learning/data_analysis/')
import C3处理与分析.pandas_def as pdef
import matplotlib.pyplot as plt

# 获取统计数据
tj = pdef.movie_year_amount_tj()
# print(tj)

# 数据的转换 dataframe -> series -> list
# 以下代码会报错 'DatetimeIndex' object has no attribute 'dt'
# years = tj.index.dt.year
# 上面的语句改成下面的实现方式
tj['year'] = tj.index
# Series.dt.year ---> 在给定Series对象的基础数据中返回日期时间的年份。
years = tj['year'].dt.year
# print(years)
amounts = tj['release_date'].tolist()
# print(amounts)

# 绘制直方图
# labels = ['G1', 'G2', 'G3']
# men_means = [20, 35, 30]
# women_means = [25, 32, 34]
# men_std = [2, 3, 4]
# women_std = [3, 5, 2]
# width = 0.35
#
# fig, ax = plt.subplots()
#
# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women')

width = 0.35
fig, ax = plt.subplots()
ax.bar(years, amounts, width)
ax.set_ylabel('Amounts of Movie')
ax.set_title('Movie Stats By Year')
# ax.legend()

plt.show()