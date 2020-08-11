"""Given inOrder and Preorder traversals of a tree, construct the tree and print postOrder traversal"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def constructTree(preorder, inorder):
  if inorder:
    root = Node(preorder.pop(0))
    root_index = inorder.index(root.data)
    root.left = constructTree(preorder, inorder[:root_index])
    root.right = constructTree(preorder, inorder[root_index + 1:])
    return root


def inOrder(root):
  if root is None:
    return
  inOrder(root.left)
  print(root.data, end=' ')
  inOrder(root.right)

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = constructTree(preorder, inorder)
inOrder(root)
