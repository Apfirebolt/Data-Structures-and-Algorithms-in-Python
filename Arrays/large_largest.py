"""Given an array find the largest and second largest number in O(n)"""

def fun(arr):
    n = len(arr)
    if n < 2:
        return -1
    if arr[0] > arr[1]:
        largest = arr[0]
        large = arr[1]
    else:
        largest = arr[1]
        large = arr[0]

    for i in range(2, n):
        if arr[i] > largest:
            large = largest
            largest = arr[i]
            continue
        if arr[i] > large:
            large = arr[i]
    return largest, large

arr = [426, 71, 426, 56, 100, 12, 17, 14, 42, 426, 18]
# arr = []
# for i in range(30):
#     temp = random.randint(1, 100)
#     arr.append(temp)
print(arr)
print()
print(fun(arr))