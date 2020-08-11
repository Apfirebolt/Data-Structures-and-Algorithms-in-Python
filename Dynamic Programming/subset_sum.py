"""Subset with a given sum, whether it exists or not"""


def hasSum(arr, target):
  n = len(arr)
  dp = [[0] * (target + 1) for i in range(n+1)]

  for i in range(n):
    dp[i][0] = 1
  for i in range(1, target):
    dp[0][i] = 0

  for i in range(1, n+1):
    for j in range(1, target+1):
      if j >= arr[i-1]:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
      else:
        dp[i][j] = dp[i-1][j]
  print(dp[n-1][target-1])

arr = [3, 4, 5, 2]
target = 6
hasSum(arr, target)
