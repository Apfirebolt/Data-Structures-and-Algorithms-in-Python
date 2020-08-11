"""
Number of bits to be flipped in order to convert 1 number into another in binary representation
"""

n1, n2 = map(int, input().split(' '))
res = str(bin(n1 ^ n2))[2:].count('1')
print(res)
