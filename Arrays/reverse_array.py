""" A program to reverse array in place without using functions or additional data structure """

arr = list(map(int, input().split(' ')))
i = 0
j = len(arr)-1

while True:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
    if i > j:
        break
print(arr)