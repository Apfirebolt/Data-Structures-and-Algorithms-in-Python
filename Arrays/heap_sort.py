"""A Program to implement heap sort in Python"""
import random
# arr = list(map(int, input().split(' ')))
arr = []
for i in range(50):
    temp = random.randint(0, 100)
    arr.append(temp)

def heapify(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, i, n)

    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

print('Before heap sort : ', arr)
heapSort(arr)
print('After heap sort : ', arr)

