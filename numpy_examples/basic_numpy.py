"""
Numpy arrays example
"""

import numpy as np

# Create a numpy array
my_list = [1, 2, 3]
x = np.array(my_list)

# Creating a matrix
my_matrix = [[1, 4, 5], [6, 3, 2], [7, 4, 1]]
two_d = np.array(my_matrix)
print(two_d)

# Arange function used to create numpy arrays, array range
np_array = np.arange(0, 5)
np_array2 = np.arange(1, 10, 2)
print('NP array 2 : ', np_array2)
print('NP array : ', np_array)

# Creating an array of zeroes/ones using numpy, pandas convert floating data by default
np_zeros = np.zeros(6)
np_ones = np.ones(4)
print('Zero array : ', np_zeros)
print('One array : ', np_ones)

# Creating 2D arrays using zeros and ones in numpy, takes argument as tuple
two_zero = np.zeros((3, 3))
two_one = np.ones((3, 4))
print(two_one)
print(two_zero)

# Using linspace, start, stop and how many numbers you want between start and end. Evenly spaced numbers
lin_space = np.linspace(0, 10, 50)
print('Lin Space array : ', lin_space)


