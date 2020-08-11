"""
Print the half diamond pattern
Input: N = 3
Output:
*
**
***
**
*
"""

def halfDiamond(n):
  printReverse = False
  for i in range(n):
    for j in range(i):
      print('*', end=' ')
    if i != 0:
      print('')

  for i in range(n):
    for j in range(i, n):
      print('*', end=' ')
    print()

n = int(input())
halfDiamond(n)