#!/usr/bin/env python


d1 = 123
d2 = 3.14
d3 = "abc"
d4 = True

print(type(d1))# <class 'int'>
print(type(d2))# <class 'float'>
print(type(d3))# <class 'str'>
print(type(d4))# <class 'bool'>

#转换数据类型
# print(int(d3))
# d3 = int(d3)
#运算
# print(d2+d3)
print(d1+d1)
print(d1-d1)
print(d1*d1)
print(d1/d1)

a = "789"
b = '890'
sum = a+b
print(sum)

# 常见数据容器
# 列表 LIST (可以有重复项) = ['physics', TRUE, 1997, TRUE, 1997]
# 集合 SET（不允许有重复值，如果有重复值，集合会自动去重）= {'physics', TRUE, 1997}
# 字典 DIC（键值对） = {'subject':'physics', 'year':1997}

s1 = "abc"
i1 = 123
f1 = 123.456
b1 = True
# 1. 创建数据容器
list1 = [s1, i1, f1, b1, s1, i1, f1, b1]
set1 = {s1, i1, f1, b1, s1, i1, f1, b1}
dict1 = {'string': s1, 'int': i1, 'float': f1, 'bool': b1}
# 2. 打印、查看数据容器
print(list1)
print(set1)
print(dict1)

print(type(list1))#<class 'list'>
print(type(set1))#<class 'set'>
print(type(dict1))#<class 'dict'>
# 3. 转换数据类型
print('---------------------------')
print(int(f1))#123
print(type(int(f1)))#<class 'int'>
print(set(list1))#{123, True, 'abc', 123.456}
print(type(set(list1)))#<class 'set'>

# 4. 查找数据、更新、删除

print('----------------------')
print(list1[0])
# print(set1[0]) #'set' object is not subscriptable
print(list(set1)[2]) # 可以先将set转为list再取值/使用for循环遍历
print(dict1)
print(dict1['string'])


# print(list1.append("append"))
# print(list1)
# print(list1.remove("append"))
# print(list1)


# print(set1.add("append"))
# print(set1)
# print(set1.remove("append"))
# print(set1)

dict1['key'] = 'appeng'
print(dict1)
del dict1['key']
print(dict1)






