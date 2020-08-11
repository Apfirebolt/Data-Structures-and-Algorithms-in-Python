"""
Calculation of Minimum length spanning Tree using Kruskal Algorithm
"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.adjacency_matrix = [[float("Inf")] * self.v for i in range(self.v)]
    self.e = []
    self.vertex_set = [-1] * vertices

  def addEdge(self, u, v, d):
    self.adjacency_matrix[u][v] = d
    self.adjacency_matrix[v][u] = d
    current_edge = [u, v, d]
    self.e.append(current_edge)

  def printEdges(self):
    for i in range(len(self.e)):
      print('Start Vertex : %d End Vertex %d : Edge Length %d ' % (self.e[i][0], self.e[i][1], self.e[i][2]))

  def printGraph(self):
    return self.adjacency_matrix

  # Function to find parent of the vertex
  def find_parent(self, v):
    if self.vertex_set[v] == -1:
      return v
    else:
      return self.find_parent(self.vertex_set[v])

  # Function to make a union of 2 vertices through adding Edge to join them
  def make_union(self, x, y):
    set_x = self.find_parent(x)
    set_y = self.find_parent(y)
    cycleFormed = []

    if set_x == set_y:
      cycleFormed = [x, y]

      # If cycle is formed then return
      return cycleFormed
    self.vertex_set[set_x] = set_y
    return cycleFormed

  def kruskalMST(self):
    min_dist = 0
    visited = set()
    sorted_edges = sorted(self.e, key=lambda x: x[2])

    for i in range(len(sorted_edges)):
      start = sorted_edges[i][0]
      end = sorted_edges[i][1]
      dist = sorted_edges[i][2]

      hasCycle = self.make_union(start, end)
      if not hasCycle and start not in visited or end not in visited:
        visited.add(sorted_edges[i][0])
        visited.add(sorted_edges[i][1])
        min_dist += dist
    return min_dist

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
print(g.kruskalMST())
