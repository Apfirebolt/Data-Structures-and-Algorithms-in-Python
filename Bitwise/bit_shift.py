""" How to perform bit shift operations in Python """

def convertBin(num):
    return bin(num)[2:]

n = int(input())
m = n << 1
o = n >> 1

print(convertBin(n))
print(convertBin(m))
print(convertBin(o))
