"""Given a sorted array of n elements, write a program to remove duplicates from it"""


def removeDuplicates(arr, n):
    index = 0
    for i in range(0, n-1):
      if arr[i] != arr[i+1]:
        arr[index] = arr[i]
        index += 1
    if arr[index] == arr[n-1]:
      index += 1

    return index

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5] 
print(removeDuplicates(arr, len(arr)))
print(arr)
