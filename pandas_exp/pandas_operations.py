"""
Custom operations provided by the pandas module.
"""

import numpy as np
import pandas as pd


def times(x):
  return x * 2

d = {'Joel': [1, 5, 10, 12],
     'Ellie': ['A', 'B', 'C', np.nan],
     'Nathan': [100, 127, 75, 127]
     }

df = pd.DataFrame(d)
print(df)

# Finding unique values for the row indexed with 'Nathan'
print(df['Nathan'].unique())

# Count of number of unique values using 'nunique' method
print(df['Nathan'].nunique())
print(df.loc[1].unique())

# Value counts method to return the frequency of each element
print(df['Nathan'].value_counts())

# Revisiting conditional selection
print(df[df['Nathan'] > 110])

# Apply method, used to apply custom method to dataframes, built in functions can also be passed
print(df['Nathan'].apply(times))
print(df['Nathan'].apply(lambda x: x + 12))

# Dropping columns by index and axis, change won't be persistent unless you provided inplace = True
print(df.drop('Nathan', axis=1))
# Printing columns of a dataframe
print(df.columns)
# Printing index information of a dataframe
print(df.index)

# Sorting on dataframes
print(df.sort_values('Nathan'))

# Finding null values in your dataframe
print(df.isnull())



