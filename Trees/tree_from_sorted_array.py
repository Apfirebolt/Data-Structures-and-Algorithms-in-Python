"""
Construct a BST from a given sorted array
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def inOrder(root):
  if not root:
    return None
  inOrder(root.left)
  print(root.data, end=' ')
  inOrder(root.right)


def sortedArrayToBST(arr):
  if not arr:
    return None
  mid = len(arr)//2
  root = Node(arr[mid])
  root.left = sortedArrayToBST(arr[:mid])
  root.right = sortedArrayToBST(arr[mid+1:])

  return root


arr = [4, 9, 16, 25, 31]
root = sortedArrayToBST(arr)
inOrder(root)