"""
Given an array A[ ] of N integers, calculate the sum of "A[i] & A[j]" of all the pairs 
formed by the given array, where & is the bitwise AND operator.
"""

arr = list(map(int, input().split(' ')))
res = 0
n = len(arr)
for i in range(n):
  for j in range(i+1, n):
    res += (arr[i] & arr[j])

print(res)