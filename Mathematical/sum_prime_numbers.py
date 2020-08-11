"""Given an integer N, find the sum of all prime numbers between 1 and N"""


def calculatePrimeSum(n):
  sieve = [True] * (n+1)
  i = 2
  while i*i < n:
    if sieve[i]:
      for j in range(2*i, n+1, i):
        sieve[j] = False
    i += 1

  primes_sum = 0
  for i in range(2, len(sieve)):
    if sieve[i]:
      primes_sum += i
  return primes_sum


n = int(input())
print(calculatePrimeSum(n))
