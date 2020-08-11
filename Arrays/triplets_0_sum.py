"""Given an array print all 3 elements of the array whose sum is 0"""

def bruteForce(arr):
  for i in range(n - 2):
    for j in range(i + 1, n - 1):
      for k in range(j + 1, n):
        if arr[i] + arr[j] + arr[k] == 0:
          print(arr[i], arr[j], arr[k])

def hashedAlgo(arr):
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
            else:
                s.add(arr[j])

# arr = list(map(int, input().split(' ')))
arr = [0, -1, 2, -3, 1]
n = len(arr)
hashedAlgo(arr)
print()
bruteForce(arr)



