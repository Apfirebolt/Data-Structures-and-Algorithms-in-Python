"""Given a linked list and a number n, calculate the sum of last n nodes of linked list"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

  def insert_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = new_node
    self.count += 1

  def printList(self):
    if not self.head:
      return
    temp = self.head
    while temp:
      print(temp.data, end=' ')
      temp = temp.next


def generateList(arr):
  q = LinkedList()
  for i in range(len(arr)):
    q.insert_node(arr[i])
  return q

def printLastNodes(linked_list, n):
  if not linked_list.head:
    return -1
  temp = linked_list.head
  cnt = 1
  nodes_sum = 0
  while cnt != (linked_list.count - n + 1):
    temp = temp.next
    cnt += 1

  while temp:
    nodes_sum += temp.data
    temp = temp.next
  return nodes_sum


arr = [5, 7, 2, 3, 9]
q = generateList(arr)
q.printList()
print()
print(printLastNodes(q, 2))
