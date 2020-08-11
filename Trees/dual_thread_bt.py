"""
Implementation of double threaded Binary Tree
"""


class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    self.isThreaded = None


class Tree:
  def __init__(self, root):
    self.root = root

  def inOrder(self, root):
    if root is None:
      return

    self.inOrder(root.left)
    print(root.data, end=' ')
    self.inOrder(root.right)

  def insert_node(self, root, data):
    new_node = Node(data)
    if root is None:
      return new_node
    if root.data > data:
      root.left = self.insert_node(root.left, data)
    else:
      root.right = self.insert_node(root.right, data)
    return root

  def convertThreaded(self, root):
    if root is None:
      return None
    if root.left is None and root.right is None:
      return root

    if root.left:
      l = self.convertThreaded(root.left)
      l.right = root
      l.isThreaded = True

    if root.right is None:
      return root

    return self.convertThreaded(root.right)




def leftMost(root):
  while root != None and root.left != None:
    root = root.left
  return root


def inOrder(root):
  if root == None:
    return
  cur = leftMost(root)

  while cur != None:
    print(cur.key, end=" ")
    if cur.isThreaded:
      cur = cur.right

    else:
      cur = leftMost(cur.right)


def createTree(arr):
  root = Node(arr[0])
  t = Tree(root)
  for i in range(1, len(arr)):
    t.root = t.insert_node(t.root, arr[i])
  return t

arr = [1, 6, 3, 9, 4, 7, 12, 16, 21]
t = createTree(arr)
t.inOrder(t.root)

print()
