"""
Check whether a number can be expressed as sum of 2 prime numbers, if yes return True
"""

total = 10000
primes = [True] * total
primes[0] = False
primes[1] = False
i = 2

while i * i <= total:
  for j in range(i*i, total, i):
    primes[j] = False
  i += 1


def primesSum(n):
  flag = False
  limit = n // 2
  for i in range(limit):
    print(i, n-i)
    if primes[i] and primes[n-i]:
      flag = True
      break
  return flag

n = int(input())
print(primesSum(n))
