"""
Given an array. The task is to choose K numbers from the array such that the absolute 
difference between the sum of chosen numbers and the sum of remaining numbers is maximum.
"""


def printMaxDiff(arr, n, k):
  arr.sort()
  min_sum = 0
  max_sum = 0
  for i in range(n):
    if i < k:
      min_sum += arr[i]
    else:
      max_sum += arr[i]
  return max_sum - min_sum

k = int(input())
arr = list(map(int, input().split(' ')))
n = len(arr)
print(printMaxDiff(arr, n, k))
