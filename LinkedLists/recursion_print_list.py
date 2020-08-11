"""A Program to print linked list in reverse order using recursion"""
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
          temp = random.randint(0, 100)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def printReverse(self, current):
      if current is None:
          return
      else:
          self.printReverse(current.next)
          print(current.data, end=' ')

l1 = LinkedList()
l1.generateList(13)
l1.printList()
print('')
l1.printReverse(l1.head)
