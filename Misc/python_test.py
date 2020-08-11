n = int(input())
s = ''

while n:
  r = n % 10
  s += str(r)
  n = n // 10

print(s)
print(s[::-1])