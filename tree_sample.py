import random


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root

    def insertNode(self, root, node):
        if root is None:
            return node

        else:
            if root.data > node.data:
                root.left = self.insertNode(root.left, node)
            else:
                root.right = self.insertNode(root.right, node)
        return root

    def preOrder(self, root):
        if root is None:
            return

        print(root.data, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=' ')

    def inOrder(self, root):
        if root is None:
            return

        self.inOrder(root.left)
        print(root.data, end=' ')
        self.inOrder(root.right)

    def generateRandomTree(self, num):
        for i in range(num):
            temp = random.randint(1, 200)
            temp_node = Node(temp)
            self.insertNode(self.root, temp_node)

n1 = Node(10)
n2 = Node(15)
n3 = Node(7)
n4 = Node(12)
n5 = Node(2)

t1 = Tree(n1)
t1.generateRandomTree(10)
t1.inOrder(t1.root)






