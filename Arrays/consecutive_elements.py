"""Given an array, return True if the array contains all consecutive elements, else false"""

arr = list(map(int, input().split(' ')))
n = len(arr)
arr_sum = 0
current_sum = 0
min_ele = min(arr)
ap_sum = n//2 * (2*min_ele + (n-1)*1)

for i in range(n):
    arr_sum += arr[i]
if arr_sum == ap_sum:
    print('Yes')
else:
    print('No')

