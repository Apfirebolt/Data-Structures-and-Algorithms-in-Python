"""Given 2 sorted arrays, merge them and print the sum of the middle elements"""

arr1 = [1, 2, 4, 6, 10]
arr2 = [4, 5, 6, 9, 12]
arr3 = []

i = 0
j = 0
n = 5

while i < n and j < n:
    if arr1[i] > arr2[j]:
        arr3.append(arr2[j])
        j += 1
    else:
        arr3.append(arr1[i])
        i += 1

if i < n:
    while i < n:
        arr3.append(arr1[i])
        i += 1

if j < n:
    while j < n:
        arr3.append(arr2[j])
        j += 1

print(arr3[n]+arr3[n-1])



