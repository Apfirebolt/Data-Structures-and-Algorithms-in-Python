"""Linked List representation of a Queue"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class QueueList:
  def __init__(self):
    self.head = None

  def enque_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = new_node

  def printQueue(self):
    if not self.head:
      return
    temp = self.head
    while temp:
      print(temp.data, end=' ')
      temp = temp.next

  def deque_node(self):
    if self.head is None:
      return None
    temp = self.head
    self.head = temp.next
    return temp


def generateList(arr):
  q = QueueList()
  for i in range(len(arr)):
    q.enque_node(arr[i])
  return q

arr = [5, 7, 2, 8]
q = generateList(arr)
q.printQueue()
print()
n1 = q.deque_node()
n2 = q.deque_node()
print(n2.data)
q.enque_node(99)
q.enque_node(54)
print()
q.printQueue()



