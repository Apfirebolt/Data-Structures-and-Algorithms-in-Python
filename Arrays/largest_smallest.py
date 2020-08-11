""" A program to find the largest and the smallest element in an array """

arr = list(map(int, input().split(' ')))
max_ele = arr[0]
min_ele = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_ele:
        max_ele = arr[i]
    if arr[i] < min_ele:
        min_ele = arr[i]

print(max_ele, min_ele)