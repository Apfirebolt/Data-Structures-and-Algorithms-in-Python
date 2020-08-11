"""Given a number, check if it is divisible by 5"""

n = int(input())
l = len(str(n))
if str(n)[l-1] == '5' or str(n)[l-1] == '0':
  print('Yes')
else:
  print('No')