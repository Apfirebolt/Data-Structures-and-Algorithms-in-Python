"""
Write a program to print full diamond pattern.
*    
**   
***  
**** 
*****
 ****
  ***
   **
    *
for a given n, here n = 5  
"""

def printFullDiamond(n):
  for i in range(n):
    for j in range(n):
      if i >= j:
        print('*', end='')
      else:
        print(' ', end='')
    print()

  for i in range(n):
    for j in range(n):
      if i >= j:
        print(' ', end='')
      else:
        print('*', end='')
    print()

printFullDiamond(5)

