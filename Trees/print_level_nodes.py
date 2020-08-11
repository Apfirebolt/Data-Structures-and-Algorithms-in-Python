"""Given a Binary Search Tree and a level, print all nodes present at this given level"""

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

  # Function to print all nodes lying at a given level of a BST
  def levelOrder(self, level):
      q = []
      start = 1
      if self.root:
         q.append(self.root)
         q.append(None)
      while len(q):
          temp = q.pop(0)
          if temp is None:
              if len(q):
                  start += 1
                  q.append(None)
          else:
              if start == level:
                  print(temp.data, end=' ')
              if temp.left:
                  q.append(temp.left)
              if temp.right:
                  q.append(temp.right)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

arr = [15, 7, 1, 9, 28, 23, 30, 20, 17]
t1 = generateTree(arr)
t1.levelOrder(2)

