"""Given a number n, return true if is a power of 4 else return False"""


def isPower(n):
  str_num = str(bin(n)[2:])
  count_one = str_num.count('1')
  count_zero = str_num.count('0')
  if count_one == 1 and count_zero % 2 == 0:
    return True
  return False

for i in range(1, 100):
  print(isPower(i), i)