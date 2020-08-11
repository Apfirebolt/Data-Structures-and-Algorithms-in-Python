"""A Program to delete n nodes after m nodes in a Linked List"""


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

# Function to delete every mth node of the linked list
def deleteEveryM(linked_list, n, m):
  list_length = linked_list.count
  if list_length < m:
    return -1

  temp = linked_list.head
  prev = None
  cnt = 1
  n_count = 1

  while temp and temp.next:
    prev = temp
    temp = temp.next
    n_count += 1
    if n_count == n:
      n_count = 1

    if cnt == m and temp:
      cnt = 1
      prev.next = temp.next
      temp = prev.next

arr = [5, 7, 2, 3, 16, 18, 10, 26, 21, 8, 99]
q = generateList(arr)
q.printList()
print()
deleteEveryM(q, 3, 5)
q.printList()

