""" Find the first repeating element in the array using hashing """

arr = list(map(int, input().split(' ')))
d = {}

for i in range(len(arr)):
    if arr[i] in d:
        print(arr[i])
        break
    else:
        d[arr[i]] = 1
