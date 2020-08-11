"""Given an array, replace every element with sum of all the elements on the right side of the array"""

arr = list(map(int, input().split(' ')))
n = len(arr)
s = 0

for i in range(n-1, -1, -1):
    temp = arr[i]
    arr[i] = s
    s += temp
print(arr)

