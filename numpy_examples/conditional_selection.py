"""
Conditional selection feature in Numpy to form new arrays using selected elements of existing array
"""

import numpy as np

arr = np.arange(0, 10)
print(arr)
bool_arr = arr > 4
print('Bool array : ', bool_arr)
new_arr = arr[bool_arr]
print('New array : ', new_arr)

# Another example
sub_array = arr[arr % 3]
print('Sub array is : ', sub_array)