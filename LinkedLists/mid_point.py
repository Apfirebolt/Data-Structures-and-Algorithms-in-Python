"""Mid point of a linked list using slow and fast pointers"""

import random

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def nextNode(self):
    return self.next

  def displayData(self):
    return self.data


class LinkedList:
  def __init__(self):
    self.head = None

  def insertNode(self, node):
    if self.head is None:
      self.head = node
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = node

  def generateList(self, num):
      for i in range(num):
          temp = random.randint(0, 20)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def findMid(self):
      if not self.head:
          return
      slow = self.head
      fast = self.head

      if not self.head.next:
          return self.head

      while True:
          fast = fast.next.next
          slow = slow.next
          # List has even number of nodes if fast pointer reaches None, odd number of nodes if fast.next is None
          if fast is None or fast.next is None:
              break
      return slow

l1 = LinkedList()
l1.generateList(2)
l1.printList()
mid_point = l1.findMid()
print('Mid point data : ', mid_point.data)