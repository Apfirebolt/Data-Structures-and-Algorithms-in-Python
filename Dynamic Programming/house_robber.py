"""House robber problem, maximum profit by stealing from houses which are not adjacent"""


def maxSteal(arr, n):
  dp = [0] * n
  dp[0] = arr[0]
  dp[1] = max(arr[0], arr[1])

  for i in range(2, n):
    dp[i] = max(arr[i] + dp[i-2], dp[i-1])

  return dp[n-1]

arr = [6, 7, 1, 3, 8, 2, 4]
n = len(arr)

print(maxSteal(arr, n))