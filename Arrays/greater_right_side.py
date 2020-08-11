"""
You are given an array A of size N. Replace every element with the next greatest element 
(greatest element on its right side) in the array. Also, since there is no element 
next to the last element, replace it with -1.
"""

def replaceRight(arr, n):
  cur_max = arr[n-1]
  arr[n-1] = -1

  for i in range(n-2, -1, -1):
    temp = arr[i]
    arr[i] = cur_max
    if temp > cur_max:
      cur_max = temp

  print(arr)



arr = list(map(int, input().split(' ')))
n = len(arr)
replaceRight(arr, n)