"""Given a number N, print numbers with all unique from 1 to N"""

n = int(input())

for i in range(n+1):
  if len(set(str(i))) == len(str(i)):
    print(i)