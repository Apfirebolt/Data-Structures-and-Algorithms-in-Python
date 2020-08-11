""" Rotate an array n times """

def leftRotate(arr):
    print(arr)
    first_ele = arr[0]

    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = first_ele
    print(arr)

def rightRotate(arr):
    print(arr)
    n = len(arr)
    last_ele = arr[n-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_ele
    print(arr)

arr = list(map(int, input().split(' ')))
rightRotate(arr)