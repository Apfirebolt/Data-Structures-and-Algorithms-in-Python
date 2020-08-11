""" Given a sum and an array, your task is to print all pairs whose sum is the given number """


def printPairs(arr, s):
    diff = set()
    for i in arr:
        diff.add(s - i)

    print(diff)

arr = list(map(int, input().split(' ')))
s = int(input())
printPairs(arr, s)
