"""Given postorder and inOrder traversal of a Tree, construct the tree and print PreOrder traversal"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def constructTree(postorder, inorder):
  if not inorder:
    return

  current_root = postorder.pop()
  print('Current is : ', current_root, inorder)
  root = Node(current_root)
  index = inorder.index(current_root)
  root.left = constructTree(postorder, inorder[:index+1])
  root.right = constructTree(postorder, inorder[index:])
  return root


def inOrder(root):
  if root is None:
    return
  inOrder(root.left)
  print(root.data, end=' ')
  inOrder(root.right)

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = constructTree(postorder, inorder)
inOrder(root)
