"""
Given an array which could contain 0 and negative numbers, determine the subarray with the max
product
"""


def maxProduct(arr, n):
  global_max = 1
  current_min = 1
  current_max = 1

  for i in range(0, n):
    # Positive number include it in current max
    if arr[i] > 0:
      current_max = arr[i]*current_max
      current_min = min(current_min*arr[i], 1)
    # Reset values if 0 is encountered
    elif arr[i] == 0:
      current_min = 1
      current_max = 1
    # For -ve values
    else:
      temp = current_max
      current_max = max(current_min*arr[i], 1)
      current_min = temp * arr[i]

    if current_max > global_max:
      global_max = current_max

  return global_max

arr = [5, 1, -6, -5, 3, -7]
# arr = list(map(int, input().split(' ')))
n = len(arr)

print(maxProduct(arr, n))