#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 2_调整视觉元素.py
@Auth: ciel7
@Date: 2022/6/16-上午9:13
@Desc: 
@Ver : 
"""

import matplotlib.pyplot as plt

# 画布
plt.figure()

# x 轴、y 轴
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]

x1 = [2, 4, 6, 8, 10, 12]
y1 = [1, 3, 4, 7, 6.5, 9]

# 轴标签
plt.xlabel("risk")
plt.ylabel("benefit")

# 标题
plt.title("Create A Figure with Multiple Elements")

# 网格
plt.grid(True)

# 数据项标识：形状、颜色
plt.scatter(x=x, y=y, color='green', marker='*', label="Sample A")
plt.scatter(x=x1, y=y1, color='red', marker='+', label="Sample B")

# 注释说明 --- label="Sample A"
plt.legend()

# 主副刻度标签
plt.xticks(ticks=[0, 4, 8, 12])
plt.yticks(ticks=[0, 3, 6, 9, 12])
plt.minorticks_on()

# 展示
plt.show()
