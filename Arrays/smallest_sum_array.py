"""
A variation of Kadane's algorithm where you have to return minimum sum of a contagious sub-array.
"""

arr = list(map(int, input().split(' ')))
n = len(arr)

min_sum = 9999
current_min = arr[0]

for i in range(1, n):
  current_min = min(arr[i], current_min + arr[i])

  if current_min < min_sum:
    min_sum = current_min

print(min_sum)