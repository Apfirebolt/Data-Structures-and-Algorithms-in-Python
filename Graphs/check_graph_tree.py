"""
An undirected graph is tree if it has following properties.
1) There is no cycle.
2) The graph is connected.
"""


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.adjacency_matrix = [[float("Inf")] * self.v for i in range(self.v)]
    self.e = []
    self.parent = [-1] * vertices

  def addEdge(self, u, v, d):
    self.adjacency_matrix[u][v] = d
    self.adjacency_matrix[v][u] = d
    current_edge = [u, v, d]
    self.e.append([u, v, d])

  def printEdges(self):
    for i in range(len(self.e)):
      print('Start Vertex : %d End Vertex %d : Edge Length %d ' % (self.e[i][0], self.e[i][1], self.e[i][2]))

  # Disjoint set method used to determine cycle exists or not
  def find_parent(self, v):
    if self.parent[v] == -1:
      return v
    else:
      return self.find_parent(self.parent[v])

  def make_union(self, u, v):
    u_set = self.find_parent(u)
    v_set = self.find_parent(v)
    cycle = False
    if u_set == v_set:
      cycle = True
    else:
      self.parent[u_set] = v_set
    return cycle

  def printGraph(self):
    return self.adjacency_matrix

  def hasCycle(self):
    contains_cycle = False
    for i in range(len(self.e)):
      start = self.e[i][0]
      end = self.e[i][1]
      contains_cycle = self.make_union(start, end)
      if contains_cycle:
        break
    return contains_cycle

  def connectedDFS(self, src):
    s = [src]
    visited = [False] * self.v
    t = set()
    isConnected = True

    while len(s):
      current = s.pop()
      visited[current] = True
      t.add(current)
      for i in range(self.v):
        if self.adjacency_matrix[current][i] != float("Inf") and not visited[i]:
          s.append(i)

    for i in range(self.v):
      if i not in t:
        isConnected = False
        break
    return isConnected

  def checkGraphTree(self):
    return self.connectedDFS(0) and not self.hasCycle()


g1 = Graph(5)
g1.addEdge(0, 2, 5)
g1.addEdge(0, 1, 3)
g1.addEdge(0, 3, 2)
g1.addEdge(3, 4, 4)
g1.addEdge(1, 2, 1)
# print(g1.connectedDFS(0))
# g1.printEdges()
# print(g1.hasCycle())
# print(g1.adjacency_matrix)
print(g1.checkGraphTree())