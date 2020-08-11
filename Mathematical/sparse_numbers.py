"""Given n, determine if the number is sparse or not"""


def isSparse(n):
  if '11' in str(bin(n)[2:]):
    return False
  else:
    return True

n = int(input())
print(isSparse(n))