"""
Given a linked list of m nodes, reverse all the nodes from the end after n nodes
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

  def traverse(self):
    if self.head is None:
      return
    temp = self.head
    while temp:
      print(temp.data, end=' ')
      temp = temp.next

  def insert_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.count += 1
      return

    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new_node
    self.count += 1

  def reverse_last(self, n):
    try:
      if n > self.count:
        raise ValueError("N cannot be greater than the length of the list!")

      if self.head is None:
        return

      temp = self.head
      cnt = 0

      while True:
        cnt += 1
        if cnt == n:
          break
        temp = temp.next

      last_node = temp
      current = temp.next
      prev = None
      next = None

      while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

      last_node.next = prev

    except Exception as Err:
      print(Err)

m = int(input())
arr = list(map(int, input().split(' ')))
n = len(arr)

l1 = LinkedList()
for ele in arr:
  l1.insert_node(ele)


# Before reversing last nodes
l1.traverse()
l1.reverse_last(m)
print()
# After reversing last nodes
l1.traverse()