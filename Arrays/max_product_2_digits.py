"""
Maximum product formed by multiplying 2 numbers given in an array which has +ve and -ve elements
"""
import sys


def maxProduct(arr):
  if arr[0] > arr[1]:
    largest = arr[0]
    large = arr[1]
  else:
    largest = arr[1]
    large = arr[0]
  n = len(arr)

  for i in range(2, n):
    if arr[i] > largest:
      large = largest
      largest = arr[i]
      continue

    elif arr[i] > large:
      large = arr[i]

  if arr[0] > arr[1]:
    smallest = arr[1]
    small = arr[0]
  else:
    smallest = arr[0]
    small = arr[1]
  n = len(arr)

  for i in range(2, n):
    print(largest, large)
    if arr[i] < smallest:
      small = smallest
      smallest = arr[i]
      continue

    elif arr[i] < small:
      small = arr[i]

  print(largest, large, smallest, small)
  return max(largest * large, smallest * small)

arr = [-2, -2, -32, -3]
# arr = list(map(int, input().split(' ')))
print(maxProduct(arr))