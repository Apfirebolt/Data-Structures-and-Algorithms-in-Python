"""
Given a string str of lowercase alphabets and an integer K, 
the task is to count all substrings of length K which have exactly K distinct characters.
"""

def countSubstrings(s, k):
  str_list = list(s)
  start = 0
  end = k - 1
  n = len(s)
  cnt = 0
  word_set = set()

  while end < n:
    for i in range(start, end+1):
      word_set.add(str_list[i])
      if len(word_set) == k:
        cnt += 1
    start += 1
    end += 1
    word_set.clear()

  return cnt

s = 'abcc'
print(countSubstrings(s, 2))
