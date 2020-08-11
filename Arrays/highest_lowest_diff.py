"""
Difference between highest and lowest occurring elements in an array, note that here we're talking 
about the frequencies of the elements not the value of the elements themselves.
"""

arr = list(map(int, input().split(' ')))
n = len(arr)
d = {}
high = -1
low = 9999
for i in range(n):
  if arr[i] not in d:
    d[arr[i]] = 1
  else:
    d[arr[i]] += 1

for key, value in d.items():
  if key > high:
    high = key
  if key < low:
    low = key

print(high - low)

