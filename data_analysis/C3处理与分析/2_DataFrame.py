#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 2_DataFrame.py
@Auth: ciel7
@Date: 2022/6/13-下午7:22
@Desc: DataFrame ---> 表格型数据结构，由 Series 构成
       操作：.loc 和 .iloc ---> 按 值、索引选取行
            df[列表] 按字段名选取列
            df[选取条件] 模糊、精确查询
@Ver : 
"""
import pandas as pd
import numpy as np

# Series
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

# DataFrame
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': s, '自定义': '自定义'}
# print(d)
df = pd.DataFrame(d)
# print(df)
# 选取：
print('---------------- 按行的索引：行号、索引值 -------------------')
# 根据行号定位
print(df.iloc[2])
# 根据值定位
print(df.loc['a'])
print('---------------- 按列的名称查询 -------------------')
# 根据行号定位
# print(df[0])
# 单列数据
print(df['two'])
print(df[['one', 'two']])
print('---------------- 行列同时进行筛选 -------------------')
print(df['two'].loc['c'])
print(df[['one', 'two']].loc['c'])

print('---------------- 模糊查询 -------------------')
print(df)
print(df[(df['one'] > 0) & (df['two'] > 0)])
# 按列的名称、行列同时进行筛选、模糊查询、精准查询

print('---------------- 精准查询 -------------------')
print(df[df['one'] == 0])
print(df[df['one'] != 3])

title = pd.Series(['泰坦尼克号', '阿甘正传', '少年的你', '霸王别姬'])
average = pd.Series([9.4, 9.5, 8.3, 9.6])
votes = pd.Series([1521458, 1568419, 1084448, 1538556])
genre = pd.Series([['剧情', '爱情'], ['剧情', '励志'], ['剧情'], ['剧情']])

# d1 = {'title': title, 'average': average, 'votes': votes, 'genre': genre}
# df1 = pd.DataFrame(d1)

df1 = pd.DataFrame(list(zip(title, average, votes, genre)), columns=['title', 'average', 'votes', 'genre'])
print('选取第2行且列标签为 title 的数据')
print(df1.iloc[2].loc['title'])
# 读取 X 列 Y 行
x = 'title'
y = 2
print(df1[x].iloc[y])