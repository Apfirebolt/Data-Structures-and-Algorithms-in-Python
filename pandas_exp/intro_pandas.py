import pandas as pd
import numpy as np


# Series can be named or datetime index instead of just numerical index
labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}

# Series from a list
series_list = pd.Series(my_list, index=labels)
print(series_list)

# Series from numpy array
series_2 = pd.Series(arr)
print('Series from array : \n', series_2)

# Creating series from a dictionary
dic_series = pd.Series(d)
print('Dictionary series : ', dic_series)

# Series holding different data types
data_series = pd.Series(data=labels)
print('Data series : ', data_series)

# Using indexes with pandas series
world_series = pd.Series([1, 2, 3, 4], index=['USA', 'India', 'China', 'Russia'])
world_series2 = pd.Series([11, 22, 30, 42], index=['Taiwan', 'India', 'Korea', 'China'])

# Adding 2 series where common keys for indexing are found.
world_series_data = world_series + world_series2
print('World Series data : ', world_series_data)
print('World Series : ', world_series)
print('Index : ', world_series['India'])