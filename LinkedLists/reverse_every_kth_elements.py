"""
You have to reverse elements of linked list in groups of size k.
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

  def insertNode(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node

    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = new_node

  def printList(self):
    if self.head is None:
      return
    else:
      temp = self.head
      while temp:
        print(temp.data, end=' ')
        temp = temp.next

  def reverseGroups(self, head, k):
    current = head
    next = None
    prev = None
    count = 0

    while (current is not None and count < k):
      next = current.next
      current.next = prev
      prev = current
      current = next
      count += 1

    if next is not None:
      head.next = self.reverseGroups(next, k)

    return prev


k = int(input())
arr = [5, 10, 12, 7, 1, 8, 2, 9]
n = len(arr)
l1 = LinkedList()

for i in range(n):
  l1.insertNode(arr[i])

l1.printList()
print()
l1.head = l1.reverseGroups(l1.head, k)
l1.printList()