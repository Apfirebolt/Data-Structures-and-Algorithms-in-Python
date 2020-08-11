"""Given a Binary Tree, convert it into it's equivalent mirror tree"""

import random


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
        q = []
        q.append(self.root)

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

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=' ')
        self.inOrder(root.right)

    def levelOrder(self):
      q = [self.root]
      while len(q):
        temp_node = q.pop(0)
        print(temp_node.data, end=' ')
        if temp_node.left:
          q.append(temp_node.left)
        if temp_node.right:
          q.append(temp_node.right)

    # Convert mirror tree
    def mirrorTree(self, root):
      if root is None:
        return

      else:
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        # Swap pointer values
        temp = root.left
        root.left = root.right
        root.right = temp

n1 = Node(15)
t1 = TreeNode(n1)
t1.insert_node(10)
t1.insert_node(21)
t1.insert_node(5)
t1.insert_node(3)

t1.levelOrder()
print()
t1.mirrorTree(t1.root)
t1.levelOrder()
