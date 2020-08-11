"""Reverse the contents of a queue"""


def reverseQueue(q):
  s = []
  while q:
    s.append(q.pop(0))
  print(s)

  while s:
    q.append(s.pop())
  print(q)

q = []
q.append(5)
q.append(12)
q.append(17)
q.append(21)
q.append(14)
reverseQueue(q)