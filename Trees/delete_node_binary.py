"""Given a binary tree, delete node with a given data assuming that it exists in the tree"""

from collections import deque


class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def set_data(self, data):
    self.data = data

  def get_data(self):
    return self.data

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right


class BinaryTree:
  def __init__(self, root):
    self.root = root

  def insert_node(self, data):
    new_node = TreeNode(data)
    d = deque()
    d.append(self.root)

    while len(d):
      # If full node, then simply pop it.
      temp_node = d.popleft()
      if temp_node.left is None:
        temp_node.left = new_node
        break
      else:
        d.append(temp_node.left)
      if temp_node.right is None:
        temp_node.right = new_node
        break
      else:
        d.append(temp_node.right)

  def levelOrder(self):
    if not self.root:
      return -1
    d = deque()
    d.append(self.root)

    while len(d):
      temp_node = d.popleft()
      print(temp_node.data, end=' ')
      if temp_node.left:
        d.append(temp_node.left)
      if temp_node.right:
        d.append(temp_node.right)

  def deleteNode(self, root, data):
    if not root:
      return root
    if root.data == data:
      if not root.left and not root.right:
        return None
      if root.right:
        root.data = root.right.data
        root.right = self.deleteNode(root.right, root.right.data)
      else:
        root.data = root.left.data
        root.left = self.deleteNode(root.left, root.left.data)

    root.left = self.deleteNode(root.left, data)
    root.right = self.deleteNode(root.right, data)
    return root

  def delete_tree(self, root):
    if not root:
      return root
    root.left = self.delete_tree(root.left)
    root.right = self.delete_tree(root.right)
    return None


n1 = TreeNode(5)
b1 = BinaryTree(n1)
b1.insert_node(7)
b1.insert_node(12)
b1.insert_node(22)
b1.insert_node(16)
b1.levelOrder()
print()
b1.root = b1.delete_tree(b1.root)
print(b1.levelOrder())