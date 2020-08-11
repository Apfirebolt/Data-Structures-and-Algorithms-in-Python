"""
Once there was a Geek he was quite intelligent and was also fond of jumping. But he jumped in a pattern like 1 leap, 2 leap, 3 leap and again from the start after 3rd leap.
1 leap means if Geek is at point P then he will jump to P+1.
2 leap means if Geek is at point P then he will jump to P+2.
3 leap means if Geek is at point P then he will jump to P+3.
You are his friend and more smarter than him. Before he starts jumping you need to tell whether he could land up to a point D or not.
Note:-He starts from point 0.
"""

n = int(input())
dp = [0]

for i in range(1, n+1):
  if i % 3 == 0:
    temp = dp[i-1] + 3
  elif i % 3 == 2:
    temp = dp[i-1] + 2
  else:
    temp = dp[i-1] + 1
  dp.append(temp)

if n not in dp:
  print('No')
else:
  print('Yes')