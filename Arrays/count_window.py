"""Given an array of integers and a number K. Find the count of distinct elements in every window of 
size K in the array."""

def windowLength(arr, n, k):
  d = {}
  result = []
  for i in range(0, k):
    if arr[i] not in d:
      d[arr[i]] = 1
    else:
      d[arr[i]] += 1

  for i in range(k, n):
    result.append(len(d))
    d[arr[i - k]] -= 1
    if d[arr[i - k]] == 0:
      d.pop(arr[i - k])

    if arr[i] not in d:
      d[arr[i]] = 1
    else:
      d[arr[i]] += 1
  result.append(len(d))
  return result


arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
n = len(arr)
print(windowLength(arr, n, k))






