#!/usr/bin/env python

sales = [
    # 商品名称
    ['雅诗兰黛', 'OLAY', '相宜本草', 'Keith'],
    # 商品销售量
    [8731, 4209, 10239, 422],
    # 商品单价
    [1099, 675, 516, 1349]
]

products = sales[0]
sales_num = sales[1]
sale_price = sales[2]

res = {}
i = 0
for p in products:
    res[p] = sales_num[i] * sale_price[i]
    i = i + 1

print(res)

price_max_name = max(res)
price_max = res[price_max_name]

print(price_max_name+':'+str(price_max))
