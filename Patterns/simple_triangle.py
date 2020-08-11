"""
Write a program which prints a simple pattern triangle
"""


def printTriangleSkew(n):
  for i in range(n):
    for j in range(0, i+1):
      print('#', end='')
    print()


def printTriangle(n):
  for i in range(n):
    for j in range(i, n):
      print('#', end='')
    print('')


n = int(input())
printTriangle(n)
printTriangleSkew(n)