"""A simple program to perform insertion sort in python"""

import random

def generateNumbers(num):
    arr = []
    for i in range(num):
        temp = random.randint(1, 50)
        arr.append(temp)
    return arr

def insertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = generateNumbers(19)
insertionSort(arr, len(arr))
print(arr)