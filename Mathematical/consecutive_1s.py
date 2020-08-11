"""Given a number n, find the maximum length of sequence containing 1s"""

import sys


def maxLengthOne(n):
  bin_list = list(str(bin(n)[2:]))
  print(bin_list)
  l = len(bin_list)
  i = 0
  cnt = 0
  max_count = -sys.maxsize
  while i < l:
    if bin_list[i] == '1':
      while bin_list[i] == '1':
        cnt += 1
        i += 1

        if i == l - 1:
          break

      if cnt > max_count:
        max_count = cnt
        cnt = 0

    else:
      i += 1
  return max_count

n = int(input())
print(maxLengthOne(n))