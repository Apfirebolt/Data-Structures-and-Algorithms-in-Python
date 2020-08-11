"""
Merging Joining and Concatenating dataframes
"""

import numpy as np
import pandas as pd

# Concatenation basically joins different dataframes together provided their dimensions must match
# By default axis is 0
# pd.concat([df1, df2, df3])

# Merging 2 dataframes much like how join is performed on SQL tables
# pd.merge(left, right, how='inner', on='key')

# Join is convenient for combining two potentially different indexed dataframes into a single dataframe.
# left.join(right, how='outer')