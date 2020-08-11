"""
Given a number n, remove consecutive repeated digits in it if they're present.
"""

def removeConsecutive(n):
  num_list = list(str(n))
  l = len(num_list)
  ans = ''
  for i in range(l-1):
    if num_list[i] != num_list[i+1]:
      ans += str(num_list[i])
    else:
      continue
  # Case to handle the last digit
  if num_list[i+1] != num_list[i]:
    ans += str(num_list[i+1])

  return ans

n = int(input())
print(removeConsecutive(n))