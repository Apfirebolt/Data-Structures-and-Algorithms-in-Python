"""A bitnoic sequence is a sequence of number which first increase and then decrease after bitonic point"""

def checkBitonic(arr):
  isBitonic = True
  n = len(arr)
  i = 0
  # Check for increasing sequence
  while True:
      if arr[i + 1] < arr[i]:
          break
      i += 1
      if i == n - 1:
          break
  # Check for decreasing sequence
  while True:
      if arr[i+1] > arr[i]:
          break
      i += 1
      if i == n-1:
          break

  if i == n - 1:
      return True
  return False

arr = [1, 7, 10, 16, 6]
print(checkBitonic(arr))
