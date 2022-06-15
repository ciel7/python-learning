# !/usr/bin/env python
# encoding: utf-8
"""
@Name: 10_练习：电影语言频数统计.py
@Auth: ciel7
@Date: 2022/6/15-上午9:39
@Desc: 
@Ver : 
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 10)

data = pd.read_csv('../data/movie_data_cleaned.csv',
                   usecols=['title', 'country', 'language', 'release_date', 'average'])

# 调整列标签的顺序
data = data[['title', 'country', 'language', 'release_date', 'average']]

# 各国每年的电影产量

data['language'] = data['language'].str.strip(' ')
data['language'] = data['language'].fillna(value='')

language_list = []
for l in data['language']:
    l_list = l.split('/')
    for label in l_list:
        label = label.strip(' ')
        language_list.append(label)

language_list = list(set(language_list))
language_list.remove('')
print(language_list)

# data['release_date'] = pd.to_datetime(data['release_date'])
# data = data.set_index(data['release_date'])
#
#
# for label in language_list:
#     temp = data[data['language'].str.contains(label)]
#
#     language_year_tj = temp['release_date'].resample('Y').count()
#
#     print(label, language_year_tj)

data_lang_tj = pd.DataFrame(np.zeros([len(language_list), 1]), index=language_list, columns=['tj'])

for i in data['language']:
    for label in language_list:
        if str(i).__contains__(label):
            data_lang_tj.loc[label, 'tj'] += 1

print(data_lang_tj)

# 将小类汇为大类，并添加至统计df
# 只做部分数据汇总演示
chinese_fy = data_lang_tj.loc['湖南话', 'tj'] \
             + data_lang_tj.loc['北京话', 'tj'] \
             + data_lang_tj.loc['西安话', 'tj'] \
             + data_lang_tj.loc['内蒙古方言', 'tj'] \
             + data_lang_tj.loc['苗语', 'tj'] \
             + data_lang_tj.loc['天津方言', 'tj'] \
             + data_lang_tj.loc['重庆方言', 'tj'] \
             + data_lang_tj.loc['唐山话', 'tj'] \
             + data_lang_tj.loc['河北井陉话', 'tj'] \
             + data_lang_tj.loc['贵州方言', 'tj'] \
             + data_lang_tj.loc['甘肃方言', 'tj'] \
             + data_lang_tj.loc['武汉话', 'tj']

data_lang_tj.loc['中国方言', 'tj'] = chinese_fy

print(data_lang_tj)
