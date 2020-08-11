"""
Given a number, determine whether it is divisible by 4 or not
"""

t = int(input())
for i in range(t):
  n = int(input())
  s = list((int(i) for i in str(n)[-2:]))
  digit_sum = s[0] * 10 + s[1]

  if digit_sum % 4 == 0 or n in [4, 8]:
    print('1')
  else:
    print('0')
