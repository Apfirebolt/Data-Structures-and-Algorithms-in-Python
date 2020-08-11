"""
Given a number n, return the product of all it's factors
"""

n = int(input())
i = 1

res = [n]
while i <= n // 2:
  if n % i == 0:
    res.append(i)
  i += 1

product = 1
for i in range(len(res)):
  product *= res[i]

print(product)