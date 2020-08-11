"""
Given a string str containing alphanumeric characters, calculate sum of 
all numbers present in the string.
"""

s = input()
res = 0
i = 0
n = len(s)
current_num = ''
while i < n:
  if ord(s[i]) >= 48 and ord(s[i]) <= 57:
    while ord(s[i]) >= 48 and ord(s[i]) <= 57:
      current_num += s[i]
      i += 1
      if i == n:
        break
    res += int(current_num)
    i += 1
    current_num = ''
  else:
    i += 1

print(res)