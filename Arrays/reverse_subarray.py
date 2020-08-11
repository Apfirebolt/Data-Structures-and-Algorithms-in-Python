"""
Provided an array of N integers, you need to reverse a subarray of that array. 
The range of this subarray is given by L and R.
"""

def reverseSubarray(arr, n, l, r):
  start = l - 1
  end = r - 1

  while True:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
    if start == end:
      break

l, r = 2, 4
arr = list(map(int, input().split(' ')))
print(arr)
reverseSubarray(arr, len(arr), l, r)
print(arr)
