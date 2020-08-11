"""
Minimum number of coins required to give away the change
"""

import sys


def minCoins(arr, m, V):
  dp = [0 for i in range(V + 1)]
  dp[0] = 0
  for i in range(1, V + 1):
    current = sys.maxsize
    for j in range(m):
      if (arr[j] <= i):
        sub_res = dp[i - arr[j]]
        if sub_res + 1 < current:
          current = sub_res + 1
        dp[i] = current
  return dp[V]


# Driver Code
if __name__ == "__main__":
  arr = [1,3,2]
  m = len(arr)
  V = 6
  print("Minimum coins required is ",
        minCoins(arr, m, V))
