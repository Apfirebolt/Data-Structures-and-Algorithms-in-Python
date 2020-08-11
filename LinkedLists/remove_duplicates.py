"""Remove duplicate nodes from a given linked list"""

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

  def removeDuplicates(self):
      temp = self.head
      ele = set()
      ele.add(self.head.data)
      while temp.next is not None:
          if temp.next.data in ele:
              temp_node = temp.next
              temp.next = temp_node.next
              del temp_node
          else:
              ele.add(temp.next.data)
          temp = temp.next
      print('Element set : ', ele)


l1 = LinkedList()
l1.generateList(40)
l1.printList()
l1.removeDuplicates()
l1.printList()
