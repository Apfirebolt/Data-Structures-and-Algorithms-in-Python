"""
Consider a devotee wishing to give offerings to temples along a mountain range. 
The temples are located in a row at different heights. Each temple should receive at least one 
offering. If two adjacent temples are at different altitudes, then the temple that is higher up 
should receive more offerings than the one that is lower down. If two adjacent temples are at the 
same height, then their offerings relative to each other does not matter. Given the number of 
temples and the heights of the temples in order, find the minimum number of offerings to bring.
"""


def minOfferings(arr, n):
  dp_inc = [1] * n
  dp_dec = [1] * n

  for i in range(1, n):
    if arr[i] > arr[i-1]:
      dp_inc[i] += dp_inc[i-1]

  for i in range(n-2, -1, -1):
    if arr[i] > arr[i+1]:
      dp_dec[i] += dp_dec[i+1]

  offering = 0
  for i in range(n):
    offering += max(dp_inc[i], dp_dec[i])

  return offering

arr = [1, 4, 3, 6, 2, 1]
n = len(arr)
print(minOfferings(arr, n))