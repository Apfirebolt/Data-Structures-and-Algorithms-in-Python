"""Matrix representation of a graph"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.adjacency_matrix = [[0] * self.v for i in range(self.v)]
    self.e = []

  def addEdge(self, u, v, d):
    self.adjacency_matrix[u][v] = d
    self.adjacency_matrix[v][u] = d
    current_edge = [(u,v), d]
    self.e.append(current_edge)

  def printEdges(self):
    for i in range(len(self.e)):
      print('Start Vertex : %d End Vertex %d : Edge Length %d ' % (self.e[i][0][0], self.e[i][0][1], self.e[i][1]))

  def printGraph(self):
    return self.adjacency_matrix


g1 = Graph(6)
g1.addEdge(0, 1, 3)
g1.addEdge(0, 2, 2)
g1.addEdge(1, 4, 7)
g1.addEdge(2, 5, 2)
g1.addEdge(2, 3, 4)
print(g1.printGraph())
g1.printEdges()



