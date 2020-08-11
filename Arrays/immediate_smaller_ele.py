"""
Given an integer array of size N. For each element in the array, check whether the right 
adjacent element (on the next immediate position) of the array is smaller. If next element 
is smaller, print that element. If not, then print -1.
"""

arr = list(map(int, input().split(' ')))
n = len(arr)
i = 0
while i < n-1:
  if arr[i+1] < arr[i]:
    arr[i] = arr[i+1]
  else:
    arr[i] = -1

  i += 1

arr[i] = -1
print(arr)


