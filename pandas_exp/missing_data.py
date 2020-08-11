"""
Dealing with missing data in pandas
"""

import numpy as np
import pandas as pd

d = {'A': [1, 2, 3, np.nan], 'B': [5, np.nan, 10, np.nan], 'C': [1, 2, 3, 12]}
df = pd.DataFrame(d)
print(df)

# Dropna method, thresh value would receive integer argument for minimum number of non-null values
# Any column having non-null values less than 3 would be deleted

print(df.dropna(axis=1, thresh=3))
print(df)

# Filling missing values, first example uses a string while the second example uses mean of a column.
print(df.fillna(value='Jake', axis=0))
print(df.fillna(value=df['A'].mean()))
