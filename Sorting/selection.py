"""A simple program to implement selection sort in python using python functions and recursion"""

import random

def selectionSort(arr):
    for i in range(len(arr)-1):
        small = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    print(arr)

def generateArray(num):
    arr = []
    for i in range(num):
        temp = random.randint(1, 40)
        arr.append(temp)
    return arr

n = int(input())
selectionSort(generateArray(n))