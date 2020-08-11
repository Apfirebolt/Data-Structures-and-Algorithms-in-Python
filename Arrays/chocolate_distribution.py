"""
Given an array of n integers where each value represents number of chocolates in a packet. 
Each packet can have variable number of chocolates. There are m students, the task is to distribute chocolate 
packets such that:

1. Each student gets one packet.
2. The difference between the number of chocolates in packet with maximum chocolates and packet with minimum 
chocolates given to the students is minimum.
"""

def minDiff(arr, m, n):
    if (m == 0 or n == 0):
        return 0
    if (n < m):
        return -1
    min_diff = sys.maxsize
    arr.sort()

    for i in range(m-1, n):
        if arr[i] - arr[i-m+1] < min_diff:
            min_diff = arr[i] - arr[i-m+1]
    return min_diff

import sys
arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
n = len(arr)


print(minDiff(arr, m, n))

