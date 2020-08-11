"""A program to determine whether a given number is a strong number or not.
Number = sum of factorials of the digit
"""
f = []


def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

for i in range(1, 10):
  current_factorial = factorial(i)
  f.append(current_factorial)


def isStrong(n):
  digits = set()
  temp = n
  while n:
    d = n % 10
    digits.add(d)
    n //= 10

  str_num = 0
  for ele in digits:
    str_num += f[ele-1]
  return str_num == temp


n = int(input())
print(isStrong(n))


