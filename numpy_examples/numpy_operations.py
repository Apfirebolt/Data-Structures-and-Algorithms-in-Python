"""
Basic operations performed using numpy
"""

import numpy as np

arr = np.arange(0, 10)
rand_array = np.random.randint(0, 100, 10)

print('Array : ', arr)
print('Random array : ', rand_array)

# Addition of 2 arrays
print(arr+rand_array)

# Element by element multiplication
print(arr * rand_array)

# Element by element subtraction
print(arr-rand_array)

# Raise every element to the power of 3
print(arr**3)

# Taking square root of every element within array
print(np.sqrt(arr))