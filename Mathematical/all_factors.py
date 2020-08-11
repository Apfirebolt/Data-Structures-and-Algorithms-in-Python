""" Write a program to print all factors of a given number """

n = int(input())
all_factors = [1, n]

i = 2

while i*i <= n:
    if n % i == 0:
        temp = n % i
        all_factors.append(i)

    i += 1
# Sort the result
all_factors.sort()
print(all_factors)


