"""Given an array A[] of N positive integers which can contain integers from 1 to N where elements can be repeated 
or can be absent from the array. Your task is to count frequency of all elements from 1 to N."""

num = int(input())
arr = list(map(int, input().split(' ')))
d = {}
n = len(arr)

for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1

result = []
for i in range(1, num+1):
    if i not in d:
        result.append(0)
    else:
        result.append(d[i])
print(result)
