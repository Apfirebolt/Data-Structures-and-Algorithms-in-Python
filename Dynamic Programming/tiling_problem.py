"""
Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board 
using the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or 
vertically i.e., as 2 x 1 tile.
"""


def numberWays(n):
  dp = [0] * n
  dp[0] = 1
  dp[1] = 2

  for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

  return dp[n-1]

n = int(input())
print(numberWays(n))