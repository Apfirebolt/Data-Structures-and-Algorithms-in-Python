"""
A Program which implements queue as linked list using 2 stacks
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class StackList:
  def __init__(self):
    self.head = None

  def insert_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    new_node.next = self.head
    self.head = new_node

  def printStack(self):
    if self.head is None:
      return -1
    temp = self.head
    while temp:
      print(temp.data, end=' ')
      temp = temp.next

  def countNodes(self):
    if not self.head:
      return 0
    cnt = 0
    temp = self.head
    while temp:
      cnt += 1
      temp = temp.next
    return cnt


class QueueList:
  def __init__(self):
    self.s1 = StackList()
    self.s2 = StackList()

  def enQueue(self, data):
    self.s1.insert_node(data)

  def deQue(self):
    if self.s2.head:
      temp = self.s2.head.data
      self.s2.head = self.s2.head.next
      return temp
    else:
      if self.s1.head is None:
        return -1
      else:
        temp = self.s1.head
        while temp:
          self.s2.insert_node(temp.data)
          temp = temp.next
        temp = self.s2.head.data
        self.s2.head = self.s2.head.next
        return temp

  def peekElement(self):
    if self.s2.head is None and self.s1.head is None:
      return -1
    else:
      temp = self.s1.head
      while temp:
        self.s1.insert_node(temp.data)
        temp = temp.next
      return self.s2.head

  def isEmpty(self):
    return self.s1.head is None and self.s2.head is None

  def queueSize(self):
    return self.s1.countNodes() + self.s2.countNodes()


q1 = QueueList()
q1.enQueue(5)
q1.enQueue(4)
print(q1.deQue())
q1.enQueue(7)
q1.enQueue(11)
q1.enQueue(8)
q1.s1.printStack()
print()
q1.s2.printStack()

