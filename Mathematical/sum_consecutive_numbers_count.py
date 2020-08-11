"""
Given a number n, print how many ways this number can be expressed as 2 or more consecutive numbers
"""

import math


def numWays(N):
  n = 2
  cnt = 0
  while True:
    a = (2*N + n - n**2)/(2*n)
    if a < 0:
      break
    if a - int(a) == 0:
      print(a, n)
      cnt += 1
    n += 1
  return cnt



n = int(input())
print(numWays(n))