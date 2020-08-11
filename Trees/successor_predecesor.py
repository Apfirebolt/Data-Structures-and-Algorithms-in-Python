"""Given a BST and a data node, if the data node exists in the tree then find the successor and predecessor"""


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


def findSuccPred(root, data):
  if root is None:
    return

  if root.data > data:
    findSuccPred.s = root
    findSuccPred(root.left, data)
  elif root.data < data:
    findSuccPred.p = root
    findSuccPred(root.right, data)
  else:
    if root.left:
      temp = root.left
      while temp.right:
        temp = temp.right
      findSuccPred.p = temp

    if root.right:
      temp = root.right
      while temp.left:
        temp = temp.left
      findSuccPred.s = temp

def generateTree(arr):
  n1 = Node(arr[0])
  t1 = Tree(n1)
  for i in range(1, len(arr)):
    t1.insert_node(t1.root, arr[i])
  return t1

arr = [15, 10, 5, 13, 21, 17]
t1 = generateTree(arr)
t1.inOrder(t1.root)

# Initializing static variables
findSuccPred.s = None
findSuccPred.p = None

findSuccPred(t1.root, 15)
print()
print(findSuccPred.s.data)
print(findSuccPred.p.data)
