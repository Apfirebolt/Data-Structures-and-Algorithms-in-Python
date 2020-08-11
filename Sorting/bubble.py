"""A Simple program in python to implement bubble sort"""

import random

def bubbleSort(arr, n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubbleSort(arr, len(arr))
print(arr)
