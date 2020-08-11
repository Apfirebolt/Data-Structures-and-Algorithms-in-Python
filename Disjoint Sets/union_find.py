"""Basic operations on Disjoint sets used for grouping points"""

from collections import defaultdict


class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = defaultdict(list)
    self.parent = [-1] * vertices

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def printGraph(self):
    return self.graph

  def parentSet(self):
    return self.parent

  def find_parent(self, i):
    if self.parent[i] == -1:
      return i
    if self.parent[i] != -1:
      return self.find_parent(self.parent[i])

  def make_union(self, x, y):
    x_set = self.find_parent(x)
    y_set = self.find_parent(y)

    self.parent[x_set] = y_set

g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

g.make_union(0, 2)
print(g.parentSet())
print(g.find_parent(0))
