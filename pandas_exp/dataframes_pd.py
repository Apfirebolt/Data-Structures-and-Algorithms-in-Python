"""
Dataframes built directly upon pandas Series, dataframes are a bunch of series having a common index
"""

import numpy as np
import pandas as pd

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# Printing individual columns through bracket notation and . notation
print(df['X'], df.W)

# Creating a new column using existing columns
df['new'] = df['W'] + df['Y']
print(df)

# Dropping this newly created column, axis = 1 denotes it's a column which we want to delete, inplace = True
# is required to make the change permanent in the dataframe

df.drop('new', axis=1, inplace=True)

# Dropping rows from dataframe, row = 0, column = 1
df.drop('E', axis=0, inplace=True)
print('Modified series : ', df)

# Returning multiple columns at once in dataframes separated by commas
print(df[['X', 'Y']])

# Returning multiple rows from the series
print(df.loc[['A', 'B']])

# Accessing rows through iloc, numerical index based access
print(df.iloc[3])

# Returning a single cell from the dataframe (row, column) notation
print(df.loc['B', 'Y'])

# Returning a subset of the dataframe
print(df.loc[['A', 'B'], ['X', 'Y', 'W']])


