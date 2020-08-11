"""A Program to delete a node in BST"""


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

  def deleteNode(self, root, data):
    if root is None:
      return root
    if data < root.data:
      root.left = self.deleteNode(root.left, data)
    elif (data > root.data):
      root.right = self.deleteNode(root.right, data)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp

      elif root.right is None:
        temp = root.left
        root = None
        return temp

      temp = root.right
      if temp.left:
        while temp.left:
          temp = temp.left
      root.data = temp.data
      root.right = self.deleteNode(root.right, temp.data)
    return root

def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

arr = [15, 7, 1, 9, 28, 23, 30, 20, 17]
t1 = generateTree(arr)
t1.inOrder(t1.root)
t1.deleteNode(t1.root, 20)
print()
t1.inOrder(t1.root)


