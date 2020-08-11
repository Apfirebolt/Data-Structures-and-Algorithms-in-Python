""" Iterative version of binary search on a sorted array """

def binarySearch(arr, data):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == data:
            return data
        if arr[mid] > data:
            high = mid-1
        else:
            low = mid + 1
    return -1

arr = list(map(int, input().split(' ')))
num = int(input())
arr.sort()

print(binarySearch(arr, num))