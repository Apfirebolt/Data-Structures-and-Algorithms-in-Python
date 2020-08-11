"""Given a Binary Tree, find the minimum and maximum values in it"""

import sys


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self, root):
    self.root = root

  def insert_node(self, data):
    new_node = Node(data)
    q = []
    q.append(self.root)

    while True:
      current_node = q.pop(0)
      if current_node.left is None:
        current_node.left = new_node
        break
      else:
        q.append(current_node.left)
      if current_node.right is None:
        current_node.right = new_node
        break

  def levelOrder(self):
    q = [self.root]
    while len(q):
      current_node = q.pop(0)
      print(current_node.data, end=' ')
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)

  def maxMin(self):
    q = [self.root]
    current_max = -sys.maxsize
    current_min = sys.maxsize

    while len(q):
      current_node = q.pop()
      if current_node.data > current_max:
        current_max = current_node.data
      if current_node.data < current_min:
        current_min = current_node.data
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)

    print(current_min, current_max)

def generateTree(arr):
  root_node = Node(arr[0])
  t1 = Tree(root_node)

  for i in range(1, len(arr)):
    t1.insert_node(arr[i])
  return t1


arr1 = [1, 6, 5, 40, 2, -15, 40, 7, 35, -8]

t1 = generateTree(arr1)
t1.levelOrder()
print()

t1.maxMin()

