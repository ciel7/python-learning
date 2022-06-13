#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 3_读取数据.py
@Auth: ciel7
@Date: 2022/6/13-下午9:19
@Desc: 
@Ver : 
"""
import pandas as pd
import numpy as np

title = pd.Series(['泰坦尼克号', '阿甘正传', '少年的你', '霸王别姬'])
average = pd.Series([9.4, 9.5, 8.3, 9.6])
votes = pd.Series([1521458, 1568419, 1084448, 1538556])
genre = pd.Series([['剧情', '爱情'], ['剧情', '励志'], ['剧情'], ['剧情']])

df = pd.DataFrame(list(zip(title, average, votes, genre)), columns=['title', 'average', 'votes', 'genre'])
print('选取第2行且列标签为 title 的数据')
# 读取 X 列 Y 行
x = 'title'
y = 2
print(df[x].iloc[y])

# 存储数据
# df.to_csv("data.csv")
df.to_excel("data.xlsx")

# 数据读取
print(pd.read_csv("data.csv"))
print(pd.read_csv("data.csv")['title'])
print(pd.read_csv("data.csv")['average'])
print(pd.read_csv("data.csv")['votes'])
print(pd.read_csv("data.csv")['genre'])