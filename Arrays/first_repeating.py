""" Given an array of elements which contains duplicate elements, return the first element which is repeated """

arr = list(map(int, input().split(' ')))
s = set()

for i in range(len(arr)):
    if arr[i] in s:
        print(arr[i])
        break
    s.add(arr[i])

