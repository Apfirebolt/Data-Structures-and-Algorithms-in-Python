"""Given a number n, find the count of set bits in it's binary representation"""

n = int(input())
s = str(bin(n)[2:])
print(s.count('1'))