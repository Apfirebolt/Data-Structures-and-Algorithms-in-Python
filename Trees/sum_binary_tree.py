"""Write a Program to print the sum of all elements of a binary tree"""


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class TreeNode:
  def __init__(self, root):
    self.root = root

  def insert_node(self, data):
    new_node = Node(data)
    q = [self.root]

    while len(q):
      current_node = q.pop(0)
      if current_node.left is None:
        current_node.left = new_node
        break
      else:
        q.append(current_node.left)
      if current_node.right is None:
        current_node.right = new_node
        break
      else:
        q.append(current_node.right)

  def levelOrder(self):
    q = [self.root]

    while len(q):
      temp = q.pop(0)
      print(temp.data, end=' ')
      if temp.left:
        q.append(temp.left)
      if temp.right:
        q.append(temp.right)

  def printSumNodes(self):
    nodes_sum = 0
    q = [self.root]
    while len(q):
      t = q.pop(0)
      nodes_sum += t.data
      if t.left:
        q.append(t.left)
      if t.right:
        q.append(t.right)

    return nodes_sum


def generateTree(arr):
  n1 = Node(arr[0])
  t1 = TreeNode(n1)

  for i in range(1, len(arr)):
    t1.insert_node(arr[i])
  return t1


arr = [1, 12, 4, 12, 18, 21, 7, 2, 7, 1, 9, 5, 3, 10, 12]
print(sum(arr))
t1 = generateTree(arr)
t1.levelOrder()
print()
print(t1.printSumNodes())
