"""
Given a sorted array arr[] of non-repeating integers without duplicates. Sort the array into a 
wave-like array and return it. In other words, arrange the elements into a sequence such 
that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).
"""

def funWave(arr, n):
    i = 0
    while i + 1 < n:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 2

arr = list(map(int, input().split(' ')))
n = len(arr)
funWave(arr, n)
print(arr)