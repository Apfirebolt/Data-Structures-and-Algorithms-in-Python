"""Given a BST, check if it is height balanced or not"""


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

    left = self.calculateHeight(root.left)
    right = self.calculateHeight(root.right)
    return 1 + max(left, right)

  def balanceFactor(self, root):
    if not root.left and not root.right:
      return 1
    left_height = self.calculateHeight(root.left)
    right_height = self.calculateHeight(root.right)
    return abs(left_height - right_height)

def generateTree(arr):
  n1 = Node(arr[0])
  t1 = Tree(n1)
  for i in range(1, len(arr)):
    t1.insert_node(t1.root, arr[i])
  return t1


arr = [15, 10, 5, 13, 21, 17]
t1 = generateTree(arr)
t1.inOrder(t1.root)
print()
print(t1.balanceFactor(t1.root))
