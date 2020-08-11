""" Given a linked list containing a loop, find the looping point and flatten the linked list """


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

  def displayList(self):
      if self.head is None:
          return
      temp = self.head
      while temp:
          print(temp.data, end=' ')
          temp = temp.next

  def detectLoop(self):
      slow = self.head
      fast = self.head

      while True:
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
              break
      return slow

n1 = Node(4)
n2 = Node(12)
n3 = Node(3)
n4 = Node(17)
n5 = Node(5)

l1 = LinkedList()
l1.insertNode(n1)
l1.insertNode(n2)
l1.insertNode(n3)
l1.insertNode(n4)
l1.insertNode(n5)

# Intentionally created a loop
n5.next = n2
# Deleting the loop through hash table where we store addresses as keys
# d = {}
# address_list = [n1, n2, n3, n4, n5]
# repeated = None
# for i in address_list:
#     if hex(id(i.next)) in d:
#         repeated = i
#         repeated.next = None
#         break
#     else:
#       d[hex(id(i.next))] = i.data

break_point = l1.detectLoop()
print(break_point.data)
break_point.next = None
l1.displayList()




