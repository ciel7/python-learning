#!/usr/bin/env python
# encoding: utf-8
"""
@Name: 1_pandas.py
@Auth: ciel7
@Date: 2022/6/13-下午6:22
@Desc: 
@Ver : 
"""

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

# 用含日期时间索引与标签的 NumPy 数组生成 DataFrame
dates = pd.date_range('20220601', periods=6)
print(dates)

# 6 行 4 列
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
