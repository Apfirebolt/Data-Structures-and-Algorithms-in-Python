"""
A Brute force method to solve the max product sub array problem
"""


def maxProduct(arr, n):
  max_p = arr[0]
  for i in range(n):
    current_p = 1
    for j in range(i, n):
      current_p = current_p * arr[j]
      if current_p > max_p:
        max_p = current_p
  return max_p

arr = list(map(int, input().split(' ')))
n = len(arr)
print(maxProduct(arr, n))

