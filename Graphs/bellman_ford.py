"""
Bellman Ford algorithm implementation to find shortest path to all nodes from a single node called source
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
    self.e.append(current_edge)

  def printEdges(self):
    for i in range(len(self.e)):
      print('Start Vertex : %d End Vertex %d : Edge Length %d ' % (self.e[i][0], self.e[i][1], self.e[i][2]))

  def printGraph(self):
    return self.adjacency_matrix

  def BellmanFord(self, src):
    n = self.v
    distance = [float("Inf")] * n
    distance[src] = 0

    for _ in range(self.v - 1):
      # Check whether a path from source to v exists through u which is of lesser distance
      for u, v, w in self.e:
        if distance[u] != float("Inf") and distance[u] + w < distance[v]:
          distance[v] = distance[u] + w

    for u, v, w in self.e:
      if distance[u] != float("Inf") and distance[u] + w < distance[v]:
        print("Graph contains negative weight cycle")
        return
    print(distance)

g = Graph(6)
g.addEdge(0, 1, 3)
g.addEdge(0, 2, 2)
g.addEdge(1, 4, 7)
g.addEdge(2, 3, 4)
g.addEdge(2, 5, 2)
g.BellmanFord(0)
