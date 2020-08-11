"""
Given an array convert it into binary tree using ADS and print inorder, preorder traversals
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None

  def insert_node(self, data):
    new_node = Node(data)
    if not self.root:
      return new_node

    q = [self.root]

    while len(q):
      current = q.pop(0)
      if current.left is None:
        current.left = new_node
        break
      else:
        q.append(current.left)

      if current.right is None:
        current.right = new_node
        break
      else:
        q.append(current.right)
    return self.root

  def inOrder(self, root):
    if root is None:
      return
    self.inOrder(root.left)
    print(root.data, end=' ')
    self.inOrder(root.right)


def createTree(arr):
  t = Tree()

  for i in range(len(arr)):
    t.root = t.insert_node(arr[i])
  return t

arr = list(map(int, input().split(' ')))
n = len(arr)

t = createTree(arr)
t.inOrder(t.root)