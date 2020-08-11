"""
The problem is to count all the possible paths from top left to bottom right of a MxN matrix 
with the constraints that from each cell you can either move to right or down.
"""

def numPaths(arr, m, n):
  for i in range(m):
    for j in range(n):
      if i == 0 or j == 0:
        arr[i][j] = 1
      else:
        arr[i][j] += ( arr[i-1][j] + arr[i][j-1] )

  return arr[m-1][n-1]

m, n = map(int, input().split(' '))
arr = [[0] * n for i in range(m)]
print(numPaths(arr, m, n))