"""
Given a graph, write a program to detect cycle in it using Disjoint sets concept
Also, print the edge which is forming the cycle
"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.e = []
    self.graph_matrix = [[0] * self.v for i in range (self.v)]
    self.parent = [-1] * self.v

  def printEdges(self):
    return self.e

  def printMatrix(self):
    return self.graph_matrix

  def parentSet(self):
    return self.parent

  # Function to find parent of the vertex
  def find_parent(self, v):
    if self.parent[v] == -1:
      return v
    else:
      return self.find_parent(self.parent[v])

  # Function to make a union of 2 vertices through adding Edge to join them
  def make_union(self, x, y):
    set_x = self.find_parent(x)
    set_y = self.find_parent(y)
    cycleFormed = []

    if set_x == set_y:
      cycleFormed = [x, y]
    self.parent[set_x] = set_y
    return cycleFormed


  def addEdge(self, u, v, d):
    self.graph_matrix[u][v] = d
    self.graph_matrix[v][u] = d
    self.e.append([u, v, d])

  def edgeCycle(self):
    hasCycle = False
    for edge in self.e:
      hasCycle = self.make_union(edge[0], edge[1])
      if len(hasCycle):
        break

    return hasCycle


g1 = Graph(3)
g1.addEdge(0, 2, 4)
g1.addEdge(0, 1, 3)
g1.addEdge(1, 2, 5)

print(g1.edgeCycle())



