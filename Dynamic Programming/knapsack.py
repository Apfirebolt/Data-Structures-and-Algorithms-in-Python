"""Classic knapsack problem"""


def knapSack(val, wt, W, n):
  dp = [[0] * (W+1) for i in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, W+1):
      if wt[i-1] <= j:
        dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i-1][j-wt[i-1]])
      else:
        dp[i][j] = dp[i-1][j]

  return dp[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(val, wt, W, n))

