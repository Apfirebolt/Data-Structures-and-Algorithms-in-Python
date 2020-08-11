"""
Given an array and a number, determine how many contiguous subarrays have sum equal to that number
"""
from collections import defaultdict


def countSubarrays(arr, s):
  d = defaultdict(lambda: 0)
  cnt = 0
  sum_array = 0

  for i in range(len(arr)):
    sum_array += arr[i]
    if sum_array == s:
      cnt += 1

    if (sum_array - s) in d:
      cnt += d[sum_array - s]
    d[sum_array] += 1
  return cnt


s = int(input())
arr = list(map(int, input().split(' ')))
n = len(arr)

print(countSubarrays(arr, s))