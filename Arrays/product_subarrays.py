"""Product of all subarrays of an array"""

arr = [10, 3, 7]
n = len(arr)
res = 1
for i in range(n):
    p = 1
    for j in range(i, n):
        p *= arr[j]
    res *= p
print(res)