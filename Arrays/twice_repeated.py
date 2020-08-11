"""Given n+2 numbers from 1 to n with any 2 numbers repeated twice, find these numbers"""

arr = [1, 2, 1, 3, 4, 3, 3, 2]
for i in range(len(arr)-1):
    if arr[abs(arr[i])] < 0:
        print(abs(arr[i]))
    else:
        arr[abs(arr[i])] = -arr[abs(arr[i])]
