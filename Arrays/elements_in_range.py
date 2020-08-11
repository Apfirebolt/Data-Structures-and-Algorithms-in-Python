"""
An array containing positive elements is given. ‘A’ and ‘B’ are two numbers defining a range. 
Write a function to check if the array contains all elements in the given range.
"""

def elementsRange(arr, a, b):
  s = set()
  flag = True
  for i in range(len(arr)):
    s.add(arr[i])

  for i in range(a, b+1):
    if i not in s:
      flag = False
      break
  return flag

n, a, b = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
print(elementsRange(arr, a, b))

