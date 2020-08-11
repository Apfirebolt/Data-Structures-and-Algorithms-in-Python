"""Given an array of scores and a total score, print how many ways we can reach to total score given the scores
in the array"""

s = 10
arr = [2, 5, 3, 6]
# arr = list(map(int, input().split(' ')))
n = len(arr)
dp = [0] * (s+1)

for i in range(n):
  current = arr[i]
  dp[current] += 1

  for j in range(current, s+1):
    dp[j] += dp[j-current]

print(dp)