"""Inorder, Preorder and Postorder Tree traversals"""

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class Tree:
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def insert_node(self, root, data):
        new_node = Node(data)
        if root is None:
            return new_node

        if data > root.data:
            root.right = self.insert_node(root.right, data)
        else:
            root.left = self.insert_node(root.left, data)
        return root

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.get_left())
        print(root.data, end=' ')
        self.inOrder(root.get_right())

    def preOrder(self, root):
        if root is None:
            return
        else:
          print(root.data, end=' ')
          self.preOrder(root.get_left())
          self.preOrder(root.get_right())

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.get_left())
        self.postOrder(root.get_right())
        print(root.data, end=' ')


def generateTree(num, data):
    n1 = Node(data)
    t1 = Tree(n1)

    for i in range(num):
        temp = random.randint(1, 100)
        t1.insert_node(t1.root, temp)
    return t1

t1 = generateTree(17, 8)
t1.preOrder(t1.root)