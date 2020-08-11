"""Given 2 values and a BST, print all the nodes whose value lie within that range"""


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

  # Function to print all nodes lying between m and n in BST
  def printRangeNodes(self, root, m, n):
    if root is None:
      return
    self.printRangeNodes(root.get_left(), m, n)
    if root.data >= m and root.data <= n:
      print(root.data, end=' ')
    self.printRangeNodes(root.get_right(), m, n)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

m, n = map(int, input().split(' '))
arr = [5, 1, 3, 7, 12, 0, 18, 4, 11, 15, 9]
t1 = generateTree(arr)
t1.inOrder(t1.root)
print()
t1.printRangeNodes(t1.root, m, n)