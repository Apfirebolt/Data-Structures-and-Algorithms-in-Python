"""Given a Binary, Tree check if this tree is BST or not"""

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

    def checkBST(self, root, min_data, max_data):
      if root is None:
        return True

      if root.data > max_data or root.data < min_data:
        return False
      return self.checkBST(root.left, min_data, root.data) and self.checkBST(root.right, root.data, max_data)


n1 = Node(15)
t1 = TreeNode(n1)
t1.insert_node(10)
t1.insert_node(21)
t1.insert_node(5)
t1.insert_node(17)
t1.inOrder(t1.root)
print()
print(t1.checkBST(t1.root, -9999, 9999))
