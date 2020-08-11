"""Given a BST containing both +ve and -ve numbers, convert this into a Sum tree"""
import random


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

  def convert_sum_tree(self, root):
      if root is None:
          return
      if not root.left and not root.right:
          return
      current_sum = 0
      if root.right:
          current_sum += root.right.data
      if root.left:
          current_sum += root.left.data
      root.data = current_sum
      self.convert_sum_tree(root.left)
      self.convert_sum_tree(root.right)


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = Tree(n1)
    for i in range(1, len(arr)):
        t1.insert_node(t1.root, arr[i])
    return t1

arr = [15, 7, 28, 23, 20, 17, 1, 9, 30]
print(arr)
t1 = generateTree(arr)
t1.inOrder(t1.root)
print()
t1.convert_sum_tree(t1.root)
t1.inOrder(t1.root)
