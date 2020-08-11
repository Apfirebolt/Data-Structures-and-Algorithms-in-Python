"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
 So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: 
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
"""


def waysCoin(arr, n, s):
  dp = [0] * (s+1)
  dp[0] = 1

  try:
    for i in range(n):
      for j in range(arr[i], s+1):
        dp[j] += dp[j - arr[i]]
  except IndexError as err:
    print(err, i, j)
  print(dp)

s = int(input())
arr = list(map(int, input().split(' ')))
waysCoin(arr, len(arr), s)



