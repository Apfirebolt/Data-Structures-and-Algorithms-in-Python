"""
Given two given numbers a and b where 1<=a<=b, find the number of perfect squares between 
a and b (a and b inclusive).
"""

import math

a, b, = map(int, input().split(' '))
x = math.ceil(math.sqrt(a))
y = math.floor(math.sqrt(b))
print(y-x+1)
