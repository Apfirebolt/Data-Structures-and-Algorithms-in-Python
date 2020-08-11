"""Given a number n, print the sum of all proper divisors of this number 
(all divisors less than this number persay)"""

def sumDivisors(n):
  i = 1
  div_sum = 0

  while True:
    if n % i == 0:
      div_sum += i
      print(i)

    if i == n // 2:
      break
    i += 1
  return div_sum

n = int(input())
print(sumDivisors(n))