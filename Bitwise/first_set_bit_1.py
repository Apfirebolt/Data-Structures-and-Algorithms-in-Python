"""Given an integer, find the position of the first set bit from the right side"""


def findPos(n):
  temp = n
  res = []
  while temp:
    c = temp % 2
    res.append(c)
    temp = temp // 2
  res.reverse()
  index = -1
  for i in range(len(res)-1, -1, -1):
    if res[i] == 1:
      index = i
      break
  return len(res)-index

n = int(input())
print(findPos(n))