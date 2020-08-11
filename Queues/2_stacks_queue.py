"""Implementation of a queue using 2 stacks through ADT"""


class Queue:
  def __init__(self):
    self.s1 = []
    self.s2 = []

  def enque(self, data):
    self.s1.append(data)

  # Remove a value from the queue
  def deque(self):
    if not len(self.s2) and not len(self.s1):
      return -1
    else:
      if len(self.s2):
        return self.s2.pop()
      else:
        while len(self.s1):
          self.s2.append(self.s1.pop())
        return self.s2.pop()

  def peekFront(self):
    if not len(self.s2) and not len(self.s1):
      return -1
    else:
      if len(self.s2):
        return self.s2[len(self.s2)-1]
      else:
        while len(self.s1):
          self.s2.append(self.s1.pop())
        return self.s2[len(self.s2)-1]

  def peekRear(self):
    if self.queueSize() == 0:
      return -1
    else:
      if self.s1:
        return self.s1[len(self.s1)-1]
      else:
        return self.s2[0]

  def isEmpty(self):
    if len(self.s1) + len(self.s2) != 0:
      return False
    else:
      return True

  def queueSize(self):
    return len(self.s1) + len(self.s2)

q = Queue()
q.enque(5)
q.enque(7)
q.enque(2)
q.enque(8)
print(q.deque())
print(q.deque())
q.enque(6)
q.enque(12)
print(q.queueSize())
print(q.peekFront())
print(q.peekRear())
