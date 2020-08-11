"""
Part 2 of the dataframe functions
"""

import numpy as np
import pandas as pd

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# Conditional selection in dataframes similar to numpy arrays
booldf = df > 0
new_df = df[booldf]
# print(df > 0)
# print(booldf)
print(new_df)
print(df['W'] > 0)
# Filtering rows using conditional selection
print(df[df['W'] > 0])

# Stacking multiple commands
print(df[df['W'] > 0][['X', 'Y']])

# Multiple conditions, use &, | operator in place of usual 'and', 'or'
print(df[(df['W'] > 0) | (df['Y'] > 1)])

# Resetting index values, does not occur inplace
print(df.reset_index())
new_index = 'CA NY WY OR CO'.split(' ')
df['States'] = new_index
print(df)

# Setting a specific column as the index of the dataframe
df.set_index('States', inplace=True)
print(df)