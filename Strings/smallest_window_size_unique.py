"""
Given a string, find the smallest window size such that it contains all the unique characters of the string
"""

def windowSize(s, n):
  letter_set = set()
  temp_set = set()
  for i in range(n):
    letter_set.add(s[i])

  start = 0
  end = len(letter_set) - 1

  while end < n:
    for i in range(start, end + 1):
      temp_set.add(s[i])
    if len(temp_set) == len(letter_set):
      break
    else:
      temp_set.clear()
      start += 1
      end += 1
  return start, end

s = input()
print(windowSize(s, len(s)))
