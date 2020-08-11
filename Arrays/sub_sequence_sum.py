"""Given an array, you need to find maximum sum of a subsequence which does not contain 2 adjacent elements"""

# arr = [5, 5, 10, 100, 10, 5]
arr = [3, 2, 7]
inc = 0
exc = 0

for i in range(0, len(arr)):
    new_exc = max(inc, exc)
    inc = exc + arr[i]
    exc = new_exc
print(max(inc, exc))
