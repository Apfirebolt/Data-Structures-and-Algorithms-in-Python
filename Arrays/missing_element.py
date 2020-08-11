""" Given an array containing numbers within a range m to n, there is one number missing find the number """
import random
m, n = map(int, input().split(' '))
arr = []

for i in range(m, n+1):
    arr.append(i)
arr_sum = sum(arr)
# Delete an element selected randomly
delIndex = random.randint(0, len(arr))
del arr[delIndex]



