"""A Program to segregate even and odd numbers in a linked list"""

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
          temp = random.randint(0, 5)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def segregateEven(self):
      if self.head is None:
        return -1
      ptr = self.head
      current = self.head

      while current:
        if current.data % 2 == 0:
          temp_data = current.data
          current.data = ptr.data
          ptr.data = temp_data
          ptr = ptr.next
        current = current.next

l1 = LinkedList()
arr = [1, 12, 17, 6, 9, 5, 7, 2, 4, 21, 28, 30, 33, 101, 111, 53]

for i in range(len(arr)):
    temp_node = Node(arr[i])
    l1.insertNode(temp_node)

l1.printList()
l1.segregateEven()
print()
l1.printList()