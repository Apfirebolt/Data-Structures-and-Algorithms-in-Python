"""Given 2 binary trees, determine whether they have the same elements in same frequency count, order may differ"""

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
    q = []
    q.append(self.root)

    while True:
      current_node = q.pop(0)
      if current_node.left is None:
        current_node.left = new_node
        break
      else:
        q.append(current_node.left)
      if current_node.right is None:
        current_node.right = new_node
        break

  def calculateSize(self, root):
    if root is None:
      return 0
    left = self.calculateSize(root.left)
    right = self.calculateSize(root.right)
    return 1 + left + right

  def inOrder(self, root):
    if root is None:
      return
    self.inOrder(root.left)
    print(root.data, end=' ')
    self.inOrder(root.right)

  def levelOrder(self):
    q = [self.root]
    while len(q):
      current_node = q.pop(0)
      print(current_node.data, end=' ')
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)


def generateTree(arr):
  root_node = Node(arr[0])
  t1 = Tree(root_node)

  for i in range(1, len(arr)):
    t1.insert_node(arr[i])
  return t1

# A Function to return True if the trees are same else False
def equalTree(t1, t2):
  d = {}
  q = [t1.root]

  while len(q):
    current_node = q.pop()
    if current_node.data not in d:
      d[current_node.data] = 1
    else:
      d[current_node.data] += 1

    if current_node.left:
      q.append(current_node.left)
    if current_node.right:
      q.append(current_node.right)

  # Check for the second tree
  q.append(t2.root)
  while len(q):
    current_node = q.pop()
    if current_node.data not in d:
      d[current_node.data] = 1
    else:
      d[current_node.data] -= 1
      if d[current_node.data] == 0:
        d.pop(current_node.data)

    if current_node.left:
      q.append(current_node.left)
    if current_node.right:
      q.append(current_node.right)

  if not len(d):
    return True

arr1 = [1, 6, 5, 4, 2, 5, 9, 7]
arr2 = [5, 2, 1, 4, 6, 7, 9, 5]

t1 = generateTree(arr1)
t2 = generateTree(arr2)
t1.levelOrder()
print()
t2.inOrder(t2.root)
if equalTree(t1, t2):
  print('True')
else:
  print('False')