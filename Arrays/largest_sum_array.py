""" Largest sum sub-array using kadane's algorithm """

arr = list(map(int, input().split(' ')))
current_max = 0
global_max = -9999

for i in range(len(arr)):
    current_max += arr[i]
    if current_max > global_max:
        global_max = current_max

    if current_max < 0:
        current_max = 0
print(global_max)
