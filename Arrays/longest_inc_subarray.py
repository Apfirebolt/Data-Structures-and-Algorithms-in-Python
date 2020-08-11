"""
Given an array containing n numbers. The problem is to find the length of the longest 
contiguous subarray such that every element in the subarray is strictly greater 
than its previous element in the same subarray. Time Complexity should be O(n).
"""

arr = list(map(int, input().split(' ')))
max_len = 1
n = len(arr)
i = 1
cnt = 1

while i < n:
  if arr[i] > arr[i-1]:
    while arr[i] > arr[i-1]:
      cnt += 1
      i += 1
      if i == n:
        break
  else:
    max_len = max(max_len, cnt)
    cnt = 1
    i += 1
print(max(max_len, cnt))

