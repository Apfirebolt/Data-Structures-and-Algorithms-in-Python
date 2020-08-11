"""
Program to remove consecutive duplicates from an array
"""
from itertools import groupby

arr = list(map(int, input().split(' ')))
n = len(arr)

print([i[0] for i in groupby(arr)])

# Another one line solution for Python
print([v for i, v in enumerate(arr) if i == 0 or v != arr[i-1]])
i = 0
while i < len(arr)-1:
    if arr[i] == arr[i+1]:
        del arr[i]
    else:
        i = i+1

print(arr)