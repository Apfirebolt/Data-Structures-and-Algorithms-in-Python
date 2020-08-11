"""
Print all the connected components of a Graph
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

  def printGraph(self):
    return self.adjacency_matrix

  # Disjoint set method used to determine cycle exists or not
  def find_parent(self, v):
    if self.parent[v] == -1:
      return v
    else:
      return self.find_parent(self.parent[v])

  def make_union(self, u, v):
    u_set = self.find_parent(u)
    v_set = self.find_parent(v)
    if u_set == v_set:
      pass
    else:
      self.parent[u_set] = v_set

  def componentDFS(self, src):
    s = [src]
    visited = [False] * self.v
    while len(s):
      current = s.pop()
      visited[current] = True
      print(current, end=' ')

      for i in range(self.v):
        if self.adjacency_matrix[current][i] != float("Inf") and not visited[i]:
          s.append(i)


  def connectedComponents(self):
    cnt = 0
    comp_parents = set()
    for i in range(len(self.e)):
      start = self.e[i][0]
      end = self.e[i][1]

      self.make_union(start, end)

    for i in range(self.v):
      p = self.find_parent(i)
      if p not in comp_parents:
        comp_parents.add(p)

    for ele in comp_parents:
      self.componentDFS(ele)
      print()
    # Each non -1 entry in parent list represents a separate component with no parent
    return self.parent.count(-1)

g1 = Graph(9)
# g1.addEdge(0, 1, 2)
# g1.addEdge(0, 4, 5)
g1.addEdge(3, 4, 4)
g1.addEdge(5, 6, 2)
g1.addEdge(7, 8, 1)
print('Number of components : ', g1.connectedComponents())
# g1.componentDFS(5)
