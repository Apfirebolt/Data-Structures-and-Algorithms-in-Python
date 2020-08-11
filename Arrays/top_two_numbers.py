""" Find the 2 greatest numbers from a list of numbers using heap and priority queue """


def heapify(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, n)

arr = list(map(int, input().split(' ')))
n = len(arr)

# Calling heapify operation on all non-leaf nodes from bottom to root
for i in range(n//2 - 1, -1, -1):
    heapify(arr, i, n)

max_ele = arr[0]
del arr[0]
for i in range(n//2 - 1, -1, -1):
    heapify(arr, i, n-1)

second_max = arr[0]
del arr[0]
print(max_ele, second_max)
