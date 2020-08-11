"""
Given a string (S) that is appended with a number at last. You need to find whether the length of string 
excluding that number is equal to that number. For example for “helloworld10”, answer is True as helloworld 
consist of 10 letters. 
"""

s = input()
n = len(s)
num = ''

for i in range(n):
  if ord(s[i]) >= 48 and ord(s[i]) <= 57:
    num += s[i]

print(1) if int(num) == len(s) - len(num) else print(0)
