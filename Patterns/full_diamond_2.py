"""
Full diamond second shape program in python
"""

def printFullDiamond(n):
  mid = n // 2
  for i in range(n):
    for j in range(n):
      if j == mid or i == mid:
        print('*', end='')
      else:
        print(' ', end='')
    print()

n = int(input())
printFullDiamond(n)