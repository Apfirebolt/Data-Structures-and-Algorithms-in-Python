"""Return first element which appears k times, -1 otherwise"""


arr = list(map(int, input().split(' ')))
k = int(input())
d = {}
n = len(arr)
result = -1
for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
        if d[arr[i]] == k:
            result = arr[i]
            break
print(result)




