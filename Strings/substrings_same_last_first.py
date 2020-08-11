"""
We are given a string S, we need to 
find count of all contiguous substrings starting and ending with same character.
"""


def printSubstrings(s):
  res = 0
  n = len(s)
  for i in range(n):
    for j in range(i, n):
      if s[i] == s[j]:
        res += 1
  return res


s = input()
print(printSubstrings(s))