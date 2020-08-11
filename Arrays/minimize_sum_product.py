"""
Given an array of even size consisting of positive integers. 
Your task is to find the sum after sorting the array, such that the sum of product of alternate elements is minimum.
"""

arr = list(map(int, input().split(' ')))
n = len(arr)
i = 0
j = n - 1
arr.sort()
prod = 0

while i < j:
  temp = arr[i] * arr[j]
  prod += temp
  i += 1
  j -= 1

print(prod)