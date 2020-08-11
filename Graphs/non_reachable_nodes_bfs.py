"""
Given an undirected graph and a set of vertices, we have to print 
all the non-reachable nodes from the given head node using a breadth-first search.
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

  def graphBFS(self, src):
    visited = [False] * self.v
    q = [src]
    reachable = []
    while len(q):
      current = q.pop(0)
      if visited[current]:
        break
      visited[current] = True
      reachable.append(current)
      for i in range(self.v):
        if self.adjacency_matrix[current][i] != float("Inf") and not visited[i]:
          q.append(i)
    return reachable

  def unreachableNodes(self, src):
    res = self.graphBFS(src)
    ans = set()
    for i in range (self.v):
      if i not in res:
        ans.add(i)
    return ans

g1 = Graph(6)
g1.addEdge(0, 2, 4)
g1.addEdge(0, 1, 5)
g1.addEdge(1, 2, 3)
g1.addEdge(3, 4, 7)
# g1.printEdges()
print(g1.unreachableNodes(1))
# print(g1.adjacency_matrix)