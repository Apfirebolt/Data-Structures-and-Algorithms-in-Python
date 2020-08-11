"""
Given a Binary tree, do a level order traversal on it in reverse order from bottom to Top
uses 1 stack and 1 queue.
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self, root):
    self.root = root

  def insert_node(self, data):
    new_node = Node(data)
    q = [self.root]

    while True:
      current = q.pop(0)
      if not current.left:
        current.left = new_node
        break
      else:
        q.append(current.left)

      if not current.right:
        current.right = new_node
        break
      else:
        q.append(current.right)

  def reverse_level_order(self):
    q = [self.root]
    s = []

    while q:
      current = q.pop(0)
      if current.right:
        q.append(current.right)
      if current.left:
        q.append(current.left)
      s.append(current)

    while s:
      current = s.pop()
      print(current.data, end=' ')

  def level_order(self):
    q = [self.root]
    while q:
      current = q.pop(0)
      print(current.data, end=' ')
      if current.left:
        q.append(current.left)
      if current.right:
        q.append(current.right)


arr = list(map(int, input().split(' ')))
n = len(arr)

root = Node(arr[0])
t1 = Tree(root)

for i in range(1, n):
  t1.insert_node(arr[i])

# Level order traversal
t1.level_order()
print()
# Reverse level order traversal
t1.reverse_level_order()
