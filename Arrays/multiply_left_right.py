"""
The task is to divide a array into two sub array (left and right) containing n/2 elements each 
and do the sum of the subarrays and then multiply both the subarrays.
"""

arr = list(map(int, input().split(' ')))
n = len(arr)
mid = n // 2
p1 = 0
p2 = 0

for i in range(n):
  if i < mid:
    p1 += arr[i]
  else:
    p2 += arr[i]

print(p1*p2)