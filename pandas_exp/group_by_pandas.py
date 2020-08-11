"""
Grouping values in pandas. Allows you to group together rows based off of a column and perform an aggregate 
functions on them.
"""

import numpy as np
import pandas as pd


d = {'Company': ['GOOGLE', 'FACEBOOK', 'MICROSOFT', 'MICROSOFT', 'FACEBOOK', 'GOOGLE'],
     'Person': ['Drake', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
     'Sales': [100, 150, 120, 220, 243, 350]
     }

df = pd.DataFrame(d)
by_company = df.groupby('Company')
print('Mean by company : \n', by_company.mean())
print('Sum : \n', by_company.sum())
print('Standard deviation : \n', by_company.std())
print('Sales by Facebook : ', by_company.sum().loc['FACEBOOK'])

# Describe method, eliciting out information in one go
print(df.groupby('Company').describe().transpose())


