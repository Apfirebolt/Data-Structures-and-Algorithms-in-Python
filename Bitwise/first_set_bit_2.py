"""Another approach to solve the first set bit problem"""


def findPos(n):
  temp = n
  cnt = 1
  while temp:
    if temp & 1:
      return cnt
    cnt += 1
    temp >>= 1
  return 0

n = int(input())
print(findPos(n))

