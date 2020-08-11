"""
Given an array arr[] of N integers, the task is to count the number of pairs with positive sum.
"""

# Efficient Method
def countPairs(arr, n):
  arr.sort()
  start = 0
  end = n-1
  cnt = 0
  while start != end:
    if arr[start] + arr[end] > 0:
      cnt += (end - start)
      end -= 1
    else:
      start += 1

arr = list(map(int, input().split(' ')))
n = len(arr)
cnt = 0
for i in range(n):
  for j in range(i+1, n):
    if arr[i] + arr[j] > 0:
      cnt += 1

print(cnt)