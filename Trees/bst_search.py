"""A recursive version of search operation on a BST"""


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

  # Function to search and return data if it exists in BST
  def searchNode(self, root, data):
      if root is None:
          return -1
      if root.data == data:
          return root.data

      if root.data > data:
          return self.searchNode(root.left, data)
      else:
          return self.searchNode(root.right, data)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

arr = [5, 1, 3, 7, 12, 0, 18, 4, 11, 15, 9]
t1 = generateTree(arr)
t1.inOrder(t1.root)
print('\nSearch 12:', t1.searchNode(t1.root, 100))
