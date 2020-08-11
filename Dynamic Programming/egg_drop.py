"""N floors and eggs, calculate minimum number of trials required to know which floors are safe to drop eggs

The following is a description of the instance of this famous puzzle involving n=2 eggs and a building with k=36 floors.
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:

…..An egg that survives a fall can be used again.
…..A broken egg must be discarded.
…..The effect of a fall is the same for all eggs.
…..If an egg breaks when dropped, then it would break if dropped from a higher floor.
…..If an egg survives a fall then it would survive a shorter fall.
…..It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th-floor do not cause an egg to break.
"""
MAX_VALUE = 235700

def eggDrop(e, f):
  dp = [[0] * (f+1) for i in range(e+1)]
  for i in range(1, e+1):
    dp[i][1] = 1
  for i in range(1, f+1):
    dp[1][i] = i

  for i in range(2, e+1):
    for j in range(2, f+1):
      min_value = MAX_VALUE
      for k in range(1, j+1):
        value = 1 + max(dp[i-1][k-1], dp[i][j-k])
        if value < min_value:
          min_value = value
      dp[i][j] = min_value
  print(dp[e][f])

e, f = map(int, input().split(' '))
eggDrop(e, f)




