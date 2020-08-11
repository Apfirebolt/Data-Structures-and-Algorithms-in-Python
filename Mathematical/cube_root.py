"""A program to print the cuberoot of a number if it exists else -1"""


def isCube(n):
  cube_root = n**(1./3.)
  if round(cube_root) ** 3 == n:
      return round(cube_root)
  else:
      return -1

n = int(input())
print(isCube(n))