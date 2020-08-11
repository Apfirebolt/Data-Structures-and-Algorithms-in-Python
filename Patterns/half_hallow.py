"""
Print this in Python 
for n = 6
# 
# # 
#   # 
#     # 
#       # 
#         # 
#       # 
#     # 
#   # 
# # 
# 
"""


def printPattern(n):
  for i in range(n+1):
    for j in range(0, i+1):
      if i > j and j != 0:
        print(' ', end='')
      else:
        print('#', end='')
    print('')
  for i in range(0, n):
    for j in range(i, n-1):
      print('#', end=' ')
    print('')

printPattern(6)



