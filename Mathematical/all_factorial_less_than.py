"""
A number N is called a factorial number if it is the factorial of a positive integer. 
For example, the first few factorial numbers are 1, 2, 6, 24, 120, …
Given a number N, the task is to print all factorial numbers smaller than or equal to N.
"""

def printNumbers(n):
  for i in range(1, n+1):
    if i in f:
      print(i, end=' ')

f = [1, 1, 2]
for i in range(3, 30):
  temp = i * f[i-1]
  f.append(temp)

n = int(input())
printNumbers(n)
