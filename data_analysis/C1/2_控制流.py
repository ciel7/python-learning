#!/usr/bin/env python

# 咖啡浓度上限
coffee_max = 10
# 咖啡浓度下限
coffee_min = 5

coffee = 7

if coffee < coffee_max and coffee > coffee_min:
    print('咖啡浓度正好，继续倒牛奶')
elif coffee > coffee_max:
    print('咖啡浓度太浓，继续倒水')
else:
    print('咖啡浓度太淡，继续倒咖啡粉')