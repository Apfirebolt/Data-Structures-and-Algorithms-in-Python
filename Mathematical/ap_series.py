""" A program which accepts the first term, number of terms and the common difference and prints the series """

a, n, d = map(int, input().split(' '))
lst = []

for i in range(n):
    temp = a + i * d
    lst.append(temp)

print(lst)