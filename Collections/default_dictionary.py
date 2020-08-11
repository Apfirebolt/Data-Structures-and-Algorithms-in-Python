"""Illustration of how default dictionary works"""


from collections import defaultdict

d = defaultdict(list)
d['amit'] = 21

# This would print empty list corresponding to this value since this does not exist.
print(d['alka'])
print(d['amit'])
