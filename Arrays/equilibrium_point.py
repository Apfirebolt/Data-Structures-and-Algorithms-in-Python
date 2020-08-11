""" Find the equilibrium point of the array such that sum of all elements on it's left is equal to sum of all 
element on it's right """

arr = [1, 2, 0, 3]
left_sum = sum(arr)
right_sum = 0
n = len(arr)

e = -1
i = 0
while i < n:
    left_sum = left_sum - arr[i]
    if i != 0:
        right_sum += arr[i-1]
    if left_sum == right_sum:
        e = i
    i += 1

print(arr[e])


