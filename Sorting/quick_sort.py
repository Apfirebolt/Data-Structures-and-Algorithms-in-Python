"""Program for quick sort"""

arr = list(map(int, input().split(' ')))

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    j = low

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

print('Before quick sort : ', arr)
quickSort(arr, 0, len(arr)-1)
print('After quick sort : ', arr)