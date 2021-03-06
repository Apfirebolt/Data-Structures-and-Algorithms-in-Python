"""Print all the nodes of a BST having only one child"""

class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

  def get_data(self):
      return self.data

  def get_left(self):
      return self.left

  def get_right(self):
      return self.right


class Tree:
  def __init__(self, root):
      self.root = root

  def get_root(self):
      return self.root

  def insert_node(self, root, data):
    new_node = Node(data)
    if root is None:
        return new_node

    if data > root.data:
        root.right = self.insert_node(root.right, data)
    else:
        root.left = self.insert_node(root.left, data)
    return root

  def inOrder(self, root):
    if root is None:
        return
    self.inOrder(root.get_left())
    print(root.data, end=' ')
    self.inOrder(root.get_right())

  def calculateHeight(self, root):
      if root is None:
          return 0
      else:
          left = self.calculateHeight(root.left)
          right = self.calculateHeight(root.right)
          return max(left, right) + 1

  def oneChildren(self, root):
      if root is None:
          return
      if root.left is not None and root.right is not None:
          self.oneChildren(root.left)
          self.oneChildren(root.right)
      elif root.right is not None:
          print(root.data, end=' ')
          self.oneChildren(root.right)
      elif root.left is not None:
          print(root.data, end=' ')
          self.oneChildren(root.left)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

arr = [17, 11, 7, 25, 18, 20, 30]
t1 = generateTree(arr)
t1.inOrder(t1.root)
print()
t1.oneChildren(t1.root)