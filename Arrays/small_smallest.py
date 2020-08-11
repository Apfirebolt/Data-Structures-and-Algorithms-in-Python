"""Given an array, return smallest and the next smallest number in O(n)"""
import random
def smallNumber(arr):
    if len(arr) == 1 or len(arr) == 0:
        return -1
    if arr[0] > arr[1]:
        smallest = arr[1]
        small = arr[0]
    else:
        smallest = arr[0]
        small = arr[1]
    n = len(arr)
    for i in range(2, n):
        if arr[i] < smallest:
            small = smallest
            smallest = arr[i]
            continue
        if arr[i] < small:
            small = arr[i]

    print(smallest, small)


# arr = list(map(int, input().split(' ')))
arr = [189, 71, 1, 56, 100, 12, 17, 14, 42, 400, 18]
# arr = []
# for i in range(30):
#     temp = random.randint(1, 100)
#     arr.append(temp)
print(arr)
print()
smallNumber(arr)