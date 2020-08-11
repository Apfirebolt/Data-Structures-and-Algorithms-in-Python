"""
A thief trying to escape from a jail has to cross N walls each with varying heights. 
He climbs X feet every time. But, due to the slippery nature of those walls, every times he 
slips back by Y feet.  Now the task is to calculate the total number of jumps required to 
cross all walls and escape from the jail.
"""


def numberClimbs(x, y, n, heights):
  cnt = 0
  i = 0
  while i < n:
    climb = 0
    current_height = heights[i]
    while True:
      climb += x
      cnt += 1

      if climb >= current_height:
        break
      else:
        climb -= y
    i += 1

  return cnt


x, y, n = 4, 1, 5
heights = [6, 9, 11, 4, 5]
# x, y, n = map(int, input().split(' '))
# heights = list(map(int, input().split(' ')))
print(numberClimbs(x, y, n, heights))