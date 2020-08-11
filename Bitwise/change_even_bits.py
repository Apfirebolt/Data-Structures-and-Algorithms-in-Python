"""
Given a number, change all bits at even positions to 0.
"""

def convertDecimal(n):
  d = 0
  pow = len(n) - 1
  for i in range(len(n)):
    if n[i] == '1':
      d += 2 ** pow
    pow -= 1
  return d

n = int(input())
bin_str = bin(n)[2:]
bin_str = list(bin_str)
res = ''
for i in range(len(bin_str)):
  if i % 2 == 0:
    bin_str[i] = 0
  if i != 0:
    res += str(bin_str[i])

print(res)
print(convertDecimal(res))

