""" Given an array, find the bitonic point in it. Assume the array is bitonic with first increasing sequence of 
numbers, then decreasing numbers """

def findBitonic(arr, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        if (arr[mid] < arr[mid + 1]):
            return findBitonic(arr, mid + 1, high);
        else:
            return findBitonic(arr, low, mid - 1);
    return -1

arr = [1, 6, 10, 14, 16, 5, 3, 2]
print(findBitonic(arr, 0, len(arr)-1))