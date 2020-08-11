"""
Given a string consisting of alphabets and others characters, 
the task is to remove all the characters other than alphabets and print the string so formed.
"""

def removeNonAlphabets(s, n):
  res = ''
  for i in range(n):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90 or ord(s[i]) >= 97 and ord(s[i]) <= 122:
      res += s[i]
  return res

s = input()
n = len(s)
print(removeNonAlphabets(s, n))
