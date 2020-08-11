"""Longest increasing subsequence problem in DP"""

def lcs(arr, n):
  dp = [1] * n

  for i in range(1, n):
    if arr[i] > arr[i - 1]:
      dp[i] += dp[i - 1]
    else:
      dp[i] = dp[i - 1]
  return dp[n - 1]


for i in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split(' ')))
  print(lcs(arr, len(arr)))