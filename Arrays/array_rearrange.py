"""Rearrange an array such that arr[i] = i, take n as input the array elements would have numbers from 1 to n-1"""

arr = list(map(int, input().split(' ')))
s = set()
n = len(arr)
for i in range(n):
    if arr[i] != -1:
        s.add(arr[i])

for i in range(n):
    if i in s:
        arr[i] = i
    else:
        arr[i] = -1

print(arr)