""" A program to separate even and odd numbers in an array with all odd numbers appearing before even numbers """

arr = list(map(int, input().split(' ')))
i = -1

for j in range(len(arr)):
    # Odd number check
    if arr[j] % 2:
        i += 1
        arr[j], arr[i] = arr[i], arr[j]

print(arr)