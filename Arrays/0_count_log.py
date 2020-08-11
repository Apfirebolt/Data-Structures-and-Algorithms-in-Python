"""Given an array of size n, sorted containing only 0 and 1 with all 1's appearing before 0"""

def returnZero(arr, low, high):
  if low <= high:
    mid = low + (high-low)//2
    if arr[mid] == 0:
      if mid == 0:
        return len(arr)
      if arr[mid-1] == 1:
        return mid
      else:
        return returnZero(arr, low, mid-1)
    else:
      return returnZero(arr, mid+1, high)
  return 0

# arr = list(map(int, input().split(' ')))
arr = [0, 0, 0, 0, 0, 0, 0]
n = len(arr)
result = returnZero(arr, 0, n-1)
print(n - result) if n != result else print(result)