"""Construct an AVL Tree from given number of nodes and then delete node from it"""


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

  def calculateHeight(self, root):
    if root is None:
      return 0

    left = self.calculateHeight(root.left)
    right = self.calculateHeight(root.right)

    return max(left, right) + 1

  def getMinValue(self, root):
    if root.left:
      temp = root.left
      if temp.left:
        while temp.left:
          temp = temp.left
      return temp
    return root

  def insert_node(self, root, data):
    new_node = Node(data)
    if root is None:
        return new_node

    if data > root.data:
        root.right = self.insert_node(root.right, data)
    else:
        root.left = self.insert_node(root.left, data)

    height = 1 + max(self.calculateHeight(root.left),
                          self.calculateHeight(root.right))

    balance = self.getBalance(root)

    if balance > 1 and data < root.left.data:
      return self.rightRotate(root)

    if balance < -1 and data > root.right.data:
      return self.leftRotate(root)

    if balance > 1 and data > root.left.data:
      root.left = self.leftRotate(root.left)
      return self.rightRotate(root)

    if balance < -1 and data < root.right.data:
      root.right = self.rightRotate(root.right)
      return self.leftRotate(root)
    return root

  def deleteNode(self, root, data):
    if root is None:
      return

    if root.data > data:
      root.left = self.deleteNode(root.left, data)
    elif root.data < data:
      root.right = self.deleteNode(root.right, data)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp
      elif root.right is None:
        temp = root.left
        root = None
        return root

      # If both children are present replace the value with the smallest node on right side
      temp = self.getMinValue(root.right)
      root.data = temp.data
      root.right = self.deleteNode(root.right, temp.data)

      balance = self.getBalance(root)
      # Case 1 - Left Left
      if balance > 1 and self.getBalance(root.left) >= 0:
        return self.rightRotate(root)

        # Case 2 - Right Right
      if balance < -1 and self.getBalance(root.right) <= 0:
        return self.leftRotate(root)

        # Case 3 - Left Right
      if balance > 1 and self.getBalance(root.left) < 0:
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)

        # Case 4 - Right Left
      if balance < -1 and self.getBalance(root.right) > 0:
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)

    return root

  def leftRotate(self, old_root):
      new_root = old_root.right
      temp = new_root.left

      # Performing rotation
      new_root.left = old_root
      old_root.right = temp

      return new_root

  def rightRotate(self, old_root):
    new_root = old_root.left
    temp = new_root.right

    # Performing rotations
    new_root.right = old_root
    old_root.left = temp

    return new_root

  def inOrder(self, root):
    if root is None:
        return
    self.inOrder(root.get_left())
    print(root.data, end=' ')
    self.inOrder(root.get_right())

  def getBalance(self, root):
    if root is None:
      return 0

    return self.calculateHeight(root.left) - self.calculateHeight(root.right)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.root = t1.insert_node(t1.root, arr[i])
    return t1

arr = [6, 9, 4, 3, 10, 2, 5, 7]
t1 = generateTree(arr)
t1.inOrder(t1.root)
print()
print(t1.getMinValue(t1.root).data)
t1.deleteNode(t1.root, 4)
print()
t1.inOrder(t1.root)
