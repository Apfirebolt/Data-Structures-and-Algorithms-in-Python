"""
Given a positive number N and a number D. Write a program to find the count of numbers 
smaller than N such that the difference between the number and sum of its digits is greater 
than or equal to given specific value D.
"""

def countNumbers(n, d):
  cnt = 0
  for i in range(1, n+1):
    k = str(i)
    if (int(k) - sum(int(x) for x in k) >= d):
      cnt += 1
  return cnt


n, d = map(int, input().split(' '))
print(countNumbers(n, d))