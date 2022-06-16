#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 1_Matplotlib入门.py
@Auth: ciel7
@Date: 2022/6/15-下午11:42
@Desc: 
@Ver : 
"""

import matplotlib.pyplot as plt

# x 轴数据
x = [1, 2, 3, 4, 5]
# Y 轴数据
y = [2.3, 3.4, 1.2, 6.6, 7.0]

# 创建一个散点图
plt.scatter(x, y, color='r', marker='+')
plt.show()
