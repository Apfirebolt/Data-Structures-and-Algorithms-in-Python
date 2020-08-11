"""List representation of a Graph undirected Graph, each node is represented as a linked list"""


class Node:
  def __init__(self, value):
    self.data = value
    self.next = None


class LinkedList:
  def __init__(self, data):
    new_node = Node(data)
    self.head = new_node

  def insert_node(self, data):
    new_node = Node(data)
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new_node

  def printList(self):
    if not self.head:
      return -1
    temp = self.head
    while temp:
      print(temp.data, end=' ')
      temp = temp.next


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.node_list = [LinkedList(i) for i in range(vertices)]

  def addEdge(self, u, v, d):
    self.node_list[u].insert_node(v)
    self.node_list[v].insert_node(u)

  def printGraph(self):
    for i in range(self.v):
      self.node_list[i].printList()
      print()

g1 = Graph(6)
g1.addEdge(0, 2, 2)
g1.addEdge(0, 1, 3)
g1.addEdge(1, 4, 7)
g1.addEdge(2, 3, 4)
g1.addEdge(2, 5, 2)
g1.printGraph()



