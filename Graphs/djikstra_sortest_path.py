"""
Djikstra algorithm to calculate sortest path from origin to every other node - 2D matrix is used for representing
Graph
"""

from collections import defaultdict
import sys


class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.matrix = [[0] * vertices for i in range(vertices)]
    self.distance_table = defaultdict(list)

  def addEdge(self, u, v, distance):
    self.matrix[u][v] = distance
    self.matrix[v][u] = distance

  def printGraph(self):
    return self.matrix

  def calculateShortest(self, source):
    self.relaxed_nodes = [source]
    distance = 0
    for i in range(self.v):
      if self.matrix[source][i] != 0:
        self.distance_table[i] = self.matrix[source][i]
      print(self.matrix[source][i], end=' ')
    print(self.distance_table)

  def minDistance(self, dist, visited_set):
    min = sys.maxsize
    for v in range(self.v):
      if dist[v] < min and visited_set[v] == False:
        min = dist[v]
        min_index = v
    return min_index

  def dijkstra(self, src):

    dist = [sys.maxsize] * self.v
    dist[src] = 0
    visited_set = [False] * self.v

    for ele in range(self.v):
      u = self.minDistance(dist, visited_set)
      visited_set[u] = True

      for v in range(self.v):
        if self.matrix[u][v] > 0 and visited_set[v] == False and dist[v] > dist[u] + self.matrix[u][v]:
          dist[v] = dist[u] + self.matrix[u][v]
    print(dist)

g = Graph(5)
g.addEdge(0, 1, 3)
g.addEdge(1, 2, 4)
g.addEdge(0, 2, 5)
g.addEdge(1, 4, 3)
g.addEdge(4, 4, 1)
g.addEdge(2, 3, 7)

g.dijkstra(2)


