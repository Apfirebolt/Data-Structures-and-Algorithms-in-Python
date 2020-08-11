"""
A number and it's reverse both are prime numbers
"""
n = 100001
primes = [True] * n


def generatePrimes():
  i = 2
  while True:
    for j in range(2*i, n, i):
      primes[j] = False
    if i * i >= n:
      break
    i += 1

generatePrimes()
num = int(input())
rev_num = int(str(num)[::-1])

if primes[num] and primes[rev_num]:
  print('Yes')
else:
  print('No')