"""
Detect a cycle in the Graph using DFS
"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.e = []
    self.graph_matrix = [[0] * self.v for i in range (self.v)]

  def addEdge(self, u, v, d):
    self.graph_matrix[u][v] = d
    self.graph_matrix[v][u] = d
    self.e.append([u, v, d])

  def printEdges(self):
    return self.e

  def printMatrix(self):
    return self.graph_matrix

  def isCyclicDFS(self, src):
    visited = [False] * self.v
    s = [src]
    isCycle = False
    while len(s):
      current_vertex = s.pop()
      if visited[current_vertex]:
        isCycle = True
        break
      visited[current_vertex] = True
      print(current_vertex, end=' ')
      for i in range(self.v):
        if self.graph_matrix[current_vertex][i] != 0 and not visited[i]:
          s.append(i)
    return isCycle


g1 = Graph(5)
g1.addEdge(0, 1, 4)
g1.addEdge(1, 2, 2)
g1.addEdge(2, 3, 7)
g1.addEdge(3, 4, 3)
# This edge creates a cycle
g1.addEdge(0, 2, 10)
print(g1.isCyclicDFS(1))

