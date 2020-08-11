"""Implementation of a queue using list in Python"""


class Queue:
  def __init__(self):
    self.q = []

  def isEmpty(self):
    return len(self.q)

  def displayQueue(self):
    return self.q

  def enque(self, data):
    self.q.append(data)

  def deque(self):
    if not len(self.q):
      return -1
    popped_ele = self.q.pop(0)
    return popped_ele

  def peekRear(self):
    return self.q[len(self.q)-1]

  def peekFront(self):
    return self.q[0]

  def countEle(self):
    return len(self.q)


q1 = Queue()
q1.enque(5)
q1.enque(7)
q1.enque(2)
q1.enque(8)
print(q1.displayQueue())
print(q1.deque())
print(q1.deque())
print(q1.displayQueue())
q1.enque(99)
q1.enque(54)
print(q1.displayQueue())
print('Total elements : ', q1.countEle())
print('Front Element : ', q1.peekFront())
print('Rear Element : ', q1.peekRear())



