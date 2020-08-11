"""
Another solution to the tidy number problem
"""


def isTidy(n):
  tidy_list = []
  temp = n
  flag = True
  while temp:
    d = temp % 10
    tidy_list.append(d)
    temp //= 10

  for i in range(len(tidy_list)-1):
    if tidy_list[i] > tidy_list[i+1]:
      flag = False
      break
  return flag

n = int(input())
print(isTidy(n))