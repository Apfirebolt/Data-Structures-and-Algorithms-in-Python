"""Given 2 linked lists, create a third linked list using their union with no duplicates allowed"""

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
          temp = random.randint(0, 16)
          temp_node = Node(temp)
          self.insertNode(temp_node)

  def printList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def sortList(self):
    if self.head is None:
      return

    current_node = self.head
    while current_node:
      smallest = current_node
      itr = current_node.next

      while itr:
        if itr.data < smallest.data:
          smallest = itr
        itr = itr.next
      # Swap values using a variable
      temp = smallest.data
      smallest.data = current_node.data
      current_node.data = temp
      current_node = current_node.next


def makeUnion(head1, head2, linked):
    ptr1 = head1
    ptr2 = head2
    s = set()

    while ptr1 and ptr2:
        if ptr1.data > ptr2.data:
            if ptr2.data not in s:
                s.add(ptr2.data)
                temp_node = Node(ptr2.data)
                linked.insertNode(temp_node)
            ptr2 = ptr2.next
        else:
            if ptr1.data not in s:
                s.add(ptr1.data)
                temp_node = Node(ptr1.data)
                linked.insertNode(temp_node)
            ptr1 = ptr1.next

    if ptr1:
        while ptr1:
            if ptr1.data not in s:
                s.add(ptr1.data)
                temp_node = Node(ptr1.data)
                linked.insertNode(temp_node)
            ptr1 = ptr1.next

    if ptr2:
        while ptr2:
            if ptr2.data not in s:
                s.add(ptr2.data)
                temp_node = Node(ptr2.data)
                linked.insertNode(temp_node)
            ptr2 = ptr2.next

l1 = LinkedList()
l1.generateList(26)
l1.sortList()
l1.printList()
l2 = LinkedList()
l2.generateList(15)
l2.sortList()
print()
l2.printList()
l3 = LinkedList()
makeUnion(l1.head, l2.head, l3)
print()
l3.printList()