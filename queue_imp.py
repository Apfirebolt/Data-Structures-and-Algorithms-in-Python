from collections import deque

q1 = deque()

# Push at the end of queue
q1.append(4)
# Push at the beginning of queue
q1.appendleft(10)
q1.append(12)
q1.appendleft(6)
q1.appendleft(7)

print(q1)
q1.popleft()
q1.pop()
print(q1)

# Extend function would add a list towards the end of the queue
q1.extend([1, 8, 11, 16, 5])
# Extend left function would add a list towards the beginning of the queue
q1.extendleft([200, 60, 53, 19, 27])
print(q1)

# Empty the queue
while len(q1):
    pass