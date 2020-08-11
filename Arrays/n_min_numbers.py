""" Find n minimum numbers from an array """
import random

def min_heapify(arr, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, n)

# arr = []
arr = list(map(int, input().split(' ')))
m = int(input())
# for i in range(50):
#     temp = random.randint(1, 1000)
#     arr.append(temp)

n = len(arr)
for i in range(n//2, -1, -1):
    min_heapify(arr, i, n)

for i in range(1, m+1):
    print(arr[0])
    del arr[0]
    min_heapify(arr, 0, n-i)

print(arr)
