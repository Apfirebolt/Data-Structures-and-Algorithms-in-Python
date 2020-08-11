"""
We are given an array and our task is to check if the elements of the array are present in 
Fibonacci series or not. Give the count of such numbers in the array.
"""

fib = [0, 1]
for i in range(2, 30):
  temp = fib[i-1] + fib[i-2]
  fib.append(temp)


def fibCount(arr, n):
  cnt = 0
  for i in arr:
    if i in fib:
      cnt += 1
  return cnt

arr = list(map(int, input().split(' ')))
n = len(arr)
print(fibCount(arr, n))
