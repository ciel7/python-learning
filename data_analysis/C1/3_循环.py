#!/usr/bin/env python

coffee = 5
coffee_standard = 20
each_time = 3

while coffee < coffee_standard:
    print('-------------------')
    print('继续加入咖啡粉：', each_time, 'g')
    print('未加入咖啡粉，当前咖啡粉含量：', coffee)
    coffee = coffee + each_time
    print('已加入咖啡粉，当前咖啡粉含量：', coffee)


# for 循环遍历销售列表中的数据，并对所有数据进行累加
sales = [123, 456, 789]
sum_sales = 0
for sale in sales:
    sum_sales += sale
print(sum_sales)