"""A Python program to delete entire linked list"""

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
          temp = random.randint(0, 50)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def deleteList(self):
      if self.head is None:
          return -1

      temp = self.head
      while temp:
          temp_node = temp
          temp = temp_node.next
          del temp_node
      self.head = None


l1 = LinkedList()
l1.generateList(10)
l1.printList()
l1.deleteList()
l1.printList()