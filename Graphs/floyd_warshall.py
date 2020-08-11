"""
All pair shortest path algorithm - Floyd warshall implementation
"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.e = []
    self.graph_matrix = [[float("Inf")] * self.v for i in range (self.v)]

  def printEdges(self):
    return self.e

  def printMatrix(self):
    return self.graph_matrix

  def addEdge(self, u, v, d):
    self.graph_matrix[u][v] = d
    self.graph_matrix[v][u] = d


    self.e.append([u, v, d])

  def floydWarshall(self):
    dist = self.graph_matrix

    for k in range(self.v):
      for i in range(self.v):
        for j in range(self.v):
          if i != j:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print(dist)

g = Graph(5)
g.addEdge(0, 1, 3)
g.addEdge(1, 2, 4)
g.addEdge(0, 2, 5)
g.addEdge(1, 4, 3)
g.addEdge(2, 3, 7)
# g1 = Graph(4)
# g1.addEdge(0, 1, 5)
# g1.addEdge(0, 3, 10)
# g1.addEdge(2, 3, 1)
# g1.addEdge(1, 2, 3)
g.floydWarshall()