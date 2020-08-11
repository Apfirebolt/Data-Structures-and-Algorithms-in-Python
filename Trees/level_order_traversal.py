"""Level order traversal of BST using deque from collections module"""

from collections import deque


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

  # Function to print level order traversal of a BST
  def levelOrder(self):
      d = deque()
      if self.root:
         d.append(self.root)
      while len(d):
          temp = d.popleft()
          print(temp.data, end=' ')
          if temp.left:
              d.append(temp.left)
          if temp.right:
              d.append(temp.right)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

arr = [17, 11, 7, 25, 18, 30, 20]
t1 = generateTree(arr)
t1.levelOrder()