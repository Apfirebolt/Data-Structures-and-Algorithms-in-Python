"""
Write a program to determine whether a given graph is bipartite graph or not. Solution of this problem using
2 way graph coloring algorithm.
"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.adjacency_matrix = [[float("Inf")] * self.v for i in range(self.v)]
    self.e = []

  def addEdge(self, u, v, d):
    self.adjacency_matrix[u][v] = d
    self.adjacency_matrix[v][u] = d
    current_edge = [u, v, d]
    self.e.append([u, v, d])

  def printEdges(self):
    for i in range(len(self.e)):
      print('Start Vertex : %d End Vertex %d : Edge Length %d ' % (self.e[i][0], self.e[i][1], self.e[i][2]))

  def printGraph(self):
    return self.adjacency_matrix

  def isBipartite(self, src):
    colors = [-1] * self.v
    colors[src] = 1
    flag = True
    q = [src]
    while len(q):
      current = q.pop()
      for i in range(self.v):
        if self.adjacency_matrix[current][i] != float("Inf") and colors[i] == -1:
          colors[i] = 1 - colors[current]
          q.append(i)

        elif self.adjacency_matrix[current][i] != float("Inf") and colors[i] == colors[current]:
          flag = False
          break
    return flag


g1 = Graph(6)
g1.addEdge(0, 1, 2)
g1.addEdge(1, 2, 3)
g1.addEdge(2, 3, 2)
g1.addEdge(3, 4, 1)

print(g1.isBipartite(0))


