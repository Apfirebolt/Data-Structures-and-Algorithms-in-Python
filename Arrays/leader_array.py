"""Print all the leaders of an array, numbers which are >= number towards their right"""

arr = [7, 4, 5, 7, 3]
max_till_now = -99
result = []

for i in range(len(arr)-1, -1, -1):
    if arr[i] >= max_till_now:
        max_till_now = arr[i]
        result.append(arr[i])

print(result[::-1])