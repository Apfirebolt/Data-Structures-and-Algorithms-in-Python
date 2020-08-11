""" Given an array, print each number and the frequency """

arr = list(map(int, input().split(' ')))
d = {}

for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1
for key, value in d.items():
    print(key, value)