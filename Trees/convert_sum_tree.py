"""Given a Binary Tree containing both +ve and -ve numbers, convert this into a Sum tree"""

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

    def convert_sum_tree(self):
        q = []
        q.append(self.root)
        while len(q):
            current_node = q.pop(0)
            if current_node.left and current_node.right:
                sum_data = current_node.left.data + current_node.right.data
                current_node.data = sum_data
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)


n1 = Node(3)
t1 = TreeNode(n1)
t1.insert_node(7)
t1.insert_node(10)
t1.insert_node(12)
t1.insert_node(1)
t1.insert_node(6)
t1.insert_node(9)
t1.inOrder(t1.root)
t1.convert_sum_tree()
print()
t1.inOrder(t1.root)

