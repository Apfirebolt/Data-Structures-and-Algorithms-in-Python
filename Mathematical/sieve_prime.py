"""Print some prime numbers in constant time using sieve algorithm"""

def printPrimes():
    primes = [True] * 10000
    for i in range(2, 100):
        if primes[i]:
            for j in range(2*i, 10000, i):
                primes[j] = False

    for i in range(len(primes)):
        if primes[i]:
            print(i, end=' ')
printPrimes()

