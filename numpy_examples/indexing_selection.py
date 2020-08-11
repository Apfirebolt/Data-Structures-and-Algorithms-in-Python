"""
Using numpy for indexing and selection
"""

import numpy as np

arr = np.arange(0, 10)
# Normal indexing and slicing would work for numpy arrays too.
print(arr[-2:])

# Setting values within a range using slicing, broadcasting
arr[0:5] = 91
print('Modified array : ', arr)

# Copying an array using numpy, python avoids creating multiple references to handle large data sets.
copy_arr = np.copy(arr)
copy_arr[1:6] = 21
print('Original array : ', arr)
print('Copied array : ', copy_arr)

# Numpy array indexing for multiple dimensions
two_d = np.array([[1, 4, 7], [2, 8, 4], [2, 7, 9]])
print(two_d[0][2], two_d[1, 2])

# Use of 2 d slicing
print(two_d[:2, 1:])

