"""
Given an array of size n and an integer b, traverse the array and if the element in array is b, 
double b and continue traversal. In the end return value of b.
"""

def valueOfB(arr, b):
  res = -1
  found = False
  for num in arr:
    if num == b:
      found = True
      b *= 2
  if found:
    return b
  else:
    return -1

b = int(input())
arr = list(map(int, input().split(' ')))
print(valueOfB(arr, b))

