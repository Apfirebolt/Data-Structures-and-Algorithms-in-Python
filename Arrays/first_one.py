"""Given a sorted array containing only 0 and 1, find the index of first 1 in O(log n)"""

def findIndex(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if mid == 0:
            if arr[mid] == 1:
                return mid
            else:
                return -1
        if arr[mid] == 1:
            if arr[mid-1] == 0:
                return mid
            else:
                high = mid - 1
        else:
            if mid + 1 < len(arr) and arr[mid+1] == 1:
                return mid + 1
            else:
                low = mid + 1
    return -1

arr = [0, 0, 0, 0, 0, 0, 1, 1]
print(findIndex(arr))
