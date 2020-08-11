"""
Given two strings s1 and s2. Modify string s1 such that all the common characters 
of s1 and s2 is to be removed and the uncommon characters of s1 and s2 is to be concatenated.
"""

s1 = input()
s2 = input()
res = ''
d = {}

for i in range(len(s2)):
  if s2[i] not in d:
    d[s2[i]] = 1
  else:
    d[s2[i]] += 1


for i in range(len(s1)):
  if s1[i] not in d:
    res += s1[i]
  else:
    d[s1[i]] = 10

for i in range(len(s2)):
  if d[s2[i]] != 10:
    res += s2[i]

print(res) if len(res) else print(-1)