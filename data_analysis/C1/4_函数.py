#!/usr/bin/env python

import numpy as np
def get_sum(list):
    sum = 0
    for s in list:
        sum += s

    return sum

list = [1,2,3,4,5,6]
sum = get_sum(list)
print(sum)

print(np.average(list))