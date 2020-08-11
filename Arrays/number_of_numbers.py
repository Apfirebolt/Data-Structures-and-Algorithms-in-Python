"""
Given an array A[]  of n elements. Your task is to complete the Function num which returns an 
integer denoting the total number of times digit k appears in the whole array.

For Example:

A[]={11,12,13,14,15}, k=1

Output=6 //Count of the digit 1 in the array
"""


def numberTimes(arr, n, k):
  cnt = 0
  for i in range(n):
    temp = str(arr[i])
    cnt += temp.count(str(k))
  return cnt

k = int(input())
arr = list(map(int, input().split(' ')))
n = len(arr)

print(numberTimes(arr, n, k))

