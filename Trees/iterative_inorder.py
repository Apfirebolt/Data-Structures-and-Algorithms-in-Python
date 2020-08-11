"""
Iterative inorder traversal of a given BST using a stack only and backtracking.
"""


class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self, root):
    self.root = root

  def insert_node(self, root, data):
    new_node = TreeNode(data)
    if root is None:
      return new_node

    if root.data > data:
      root.left = self.insert_node(root.left, data)
    else:
      root.right = self.insert_node(root.right, data)
    return root

  def inOrder(self, root):
    if root is None:
      return
    self.inOrder(root.left)
    print(root.data, end=' ')
    self.inOrder(root.right)


def createTree(arr):
  n1 = TreeNode(arr[0])
  t1 = Tree(n1)

  for i in range(1, len(arr)):
    t1.insert_node(t1.root, arr[i])
  return t1


def stackPrint(root):
  s = []
  current = root
  while True:
    if current is not None:
      s.append(current)
      current = current.left
    elif s:
      current = s.pop()
      print(current.data, end=' ')
      current = current.right
    else:
      break


arr = [7, 5, 19, 21, 9, 17]
t1 = createTree(arr)
t1.inOrder(t1.root)
print()
stackPrint(t1.root)
print()
# Verify results using recursive traversal technique
t1.inOrder(t1.root)

