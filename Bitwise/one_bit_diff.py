"""
Given two non-negative integers a and b. The problem is to check whether the two 
numbers differ at one bit position only or not.
"""

a, b = map(int, input().split(' '))
c = a ^ b
cnt = 0

while c:
  if c & 1:
    cnt += 1
    print(c)
  c >>= 1

if cnt == 1:
  print('Yes')
else:
  print('No')