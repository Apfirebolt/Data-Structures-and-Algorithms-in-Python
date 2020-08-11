"""
Part 3 of the dataframes discussion series
"""

import numpy as np
import pandas as pd

# Multi level series in pandas and how to access them
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))

# Function returns multilevel index in pandas
hier_index = pd.MultiIndex.from_tuples(hier_index)
# Printing the levels of the multi level indexing
print(hier_index.levels)
print(hier_index)

# Creating the dataframe
df = pd.DataFrame(np.random.randn(6, 2), hier_index, ['A', 'B'])
print(df)

# Accessing elements, start from outside
print(df.loc['G1'])
print(df.loc['G1'].loc[1])

# Naming indices
df.index.names = ['Groups', 'Numbers']
print(df)
# Accessing individual cells
print(df.loc['G1'].loc[1]['B'])

# Cross section function, ability to go inside and print element at a given index for all groups
print(df.xs('G1'))
print(df.xs(1, level='Numbers'))

