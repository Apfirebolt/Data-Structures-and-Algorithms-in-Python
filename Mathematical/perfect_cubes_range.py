"""
Given two given numbers a and b where 1<=a<=b, find the perfect 
cubes between a and b (a and b inclusive).
"""

cubes = []
for i in range(1, 23):
  cubes.append(pow(i, 3))

def cubesRange(a, b):
  found = False
  res = []
  for ele in cubes:
    if ele >= a and ele <= b:
      found = True
      res.append(ele)

  if not found:
    print('No')
  else:
    for ele in res:
      print(ele, end=' ')

a, b = map(int, input().split(' '))
cubesRange(a, b)
