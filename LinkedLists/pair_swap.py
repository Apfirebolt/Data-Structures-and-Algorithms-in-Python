"""Program to pair wise swap linked list nodes"""

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
          temp = random.randint(0, 30)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def pairSwap(self):
      if self.head is None:
          return -1

      prev = None
      current = self.head

      while current and current.next:
          temp = current.data
          current.data = current.next.data
          current.next.data = temp

          current = current.next.next

l1 = LinkedList()
arr = [2, 7, 2, 8, 1, 9, 5, 1, 0]
for i in range(len(arr)):
    temp_node = Node(arr[i])
    l1.insertNode(temp_node)
l1.printList()
l1.pairSwap()
print()
l1.printList()