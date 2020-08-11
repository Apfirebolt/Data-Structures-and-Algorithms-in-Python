"""A linked list program to delete alternate nodes"""

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
          temp = random.randint(0, 6)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def deleteAlternate(self):
      if self.head is None:
          return

      prev = self.head
      now = self.head.next

      while prev is not None and now is not None:
          prev.next = now.next
          now = None

          prev = prev.next
          if (prev != None):
              now = prev.next


l1 = LinkedList()
l1.generateList(5)
# n1 = Node(3)
# n2 = Node(5)
# n3 = Node(4)
# n4 = Node(5)
# n5 = Node(1)
# l1.insertNode(n1)
# l1.insertNode(n2)
# l1.insertNode(n3)
# l1.insertNode(n4)
# l1.insertNode(n5)
l1.printList()
print()
l1.deleteAlternate()
l1.printList()