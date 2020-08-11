"""Rod cutting problem in DP"""


def cutRod(arr, n):
  dp = [0] * (n + 1)
  dp[0] = 0

  for i in range(1, n+1):
    max_value = -100000
    for j in range(i):
      max_value = max(max_value, arr[j] + dp[i-j-1])
    dp[i] = max_value
  return dp[n]


arr = [1, 5, 8]
size = len(arr)
print(cutRod(arr, size))