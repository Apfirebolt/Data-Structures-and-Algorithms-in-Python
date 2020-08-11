"""
Given a positive integer N. The task is to check whether this integer has an 
alternate pattern of 0 and 1 in its binary representation or not.
"""

t = int(input())
for i in range(t):
  n = int(input())
  s = bin(n)[2:]
  flag = True
  l = len(s)
  for i in range(0, l - 1):
    if s[i] == '1' and s[i + 1] == '1' or s[i] == '0' and s[i + 1] == '0':
      flag = False
      break
  if flag:
    print(1)
  else:
    print(0)
