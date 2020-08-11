""" Recursive version of binary search """

def binarySearch(arr, num, low, high):
    # Base condition when element is not found
    if low > high:
        return -1

    mid = low + (high- low) // 2
    if arr[mid] == num:
        return num
    if arr[mid] > num:
        return binarySearch(arr, num, low, mid-1)
    else:
        return binarySearch(arr, num, mid+1, high)

arr = list(map(int, input().split(' ')))
num = int(input())
arr.sort()

print(binarySearch(arr, num, 0, len(arr)-1))