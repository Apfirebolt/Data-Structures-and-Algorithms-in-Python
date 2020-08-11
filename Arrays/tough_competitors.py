"""
There are N competitors in an exam .Each competitor has his own skill value which is given 
by the array s=s1,s2,....sN where s1 is the skill of the first competitor,s2 is the skill of 
second competitor and so on.. Two competitors are said to be tough competitors if their skill 
difference is least i.e. they are very close in their skill values.Given N and an array s as 
input,find the tough competitors among the N competitors and print the absolute of the difference 
of their skill values.
"""
import sys


arr = list(map(int, input().split(' ')))
n = len(arr)

arr.sort()
min_diff = sys.maxsize

for i in range(n-1):
  if arr[i+1] - arr[i] < min_diff:
    min_diff = arr[i+1] - arr[i]

print(min_diff)
