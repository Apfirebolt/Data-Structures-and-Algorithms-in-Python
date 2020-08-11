"""
Given 2 numbers n and m, print all the stepping numbers within this range. Numbers where difference between
adjacent digit is not more than 1
"""


def printStepping(m, n):
  for i in range(m, n+1):
    isStep = True
    current = str(i)
    for j in range(len(current)-1):
      if abs(int(current[j]) - int(current[j+1])) != 1:
        isStep = False
        break
    if isStep:
      print(i)


m, n = map(int, input().split(' '))
printStepping(m, n)