"""
Implementation of a single threaded binary Tree - Right Null Pointer
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self, root):
    self.root = root

  def isLeaf(self, root):
    if not root:
      return True
    if root.left is None and root.right is None:
      return True
    return False

  def calculateHeight(self, root):
    if root is None:
      return 0
    else:
      left = self.calculateHeight(root.left)
      right = self.calculateHeight(root.right)

      return max(left, right) + 1

  def insert_node(self, root, data):
    new_node = Node(data)
    if root is None:
      return new_node

    if root.data > data:
      root.left = self.insert_node(root.left, data)
    else:
      root.right = self.insert_node(root.right, data)
    return root

  def inOrder(self, root):
    if root is None:
      return
    self.inOrder(root.left)
    print(root.data, end=' ')
    self.inOrder(root.right)


def generateTree(arr):
  root = Node(arr[0])
  t = Tree(root)
  for i in range(1, len(arr)):
    root = t.insert_node(root, arr[i])
  return t

arr = [17, 12, 27, 5, 14, 2, 7, 19, 31]
t = generateTree(arr)
t.inOrder(t.root)