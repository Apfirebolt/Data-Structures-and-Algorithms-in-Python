"""Given an integer, check if it is power of 3 or not"""

def isPower3(n):
  if n == 0:
    return False
  while n is not 1:
    if n % 3:
      return False
    n //= 3
  return True

n = int(input())
print(isPower3(n))