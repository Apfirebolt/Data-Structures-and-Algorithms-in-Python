"""Given an array, replace each element with the product of entire array except itself"""

arr = [2, 7, 5]
n = len(arr)
p = 1

for i in range(n):
  p *= arr[i]

for i in range(n):
  arr[i] = p // arr[i]

print(arr)