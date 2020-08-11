"""
Tidy numbers having digits in non-decreasing order
"""

n = int(input())
s = str(n)
flag = True

for i in range(len(s)-1):
  if int(s[i]) > int(s[i+1]):
    flag = False
    break

if flag:
  print('1')
else:
  print('0')