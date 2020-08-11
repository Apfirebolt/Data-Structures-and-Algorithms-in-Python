"""A majority element is an element which occurs in an array more than n / 2 times"""

import math


def returnMajority(arr, n, limit):
  for i in range(n):
    if arr[i] not in d:
      d[arr[i]] = 1

    else:
      d[arr[i]] += 1
      if d[arr[i]] == limit:
        return arr[i]
  return -1

arr = list(map(int, input().split(' ')))
n = len(arr)
limit = math.ceil(n / 2)
d = {}
print(returnMajority(arr, n, limit))
