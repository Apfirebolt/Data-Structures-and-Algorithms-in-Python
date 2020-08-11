""" Given an array A of positive integers. Count number of smaller elements on right side of each array. """

arr = list(map(int, input().split(' ')))
n = len(arr)
result = []
for i in range(0, n-1):
    cnt = 0
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            cnt += 1
    result.append(cnt)
result.append(0)
print(result)