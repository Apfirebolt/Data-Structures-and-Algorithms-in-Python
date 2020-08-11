
class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root

    def findMinNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def insertNode(self, root, node):
        if root is None:
            return node

        if root.data > node.data:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)

        return root

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    def preOrder(self, root):
        if root is None:
            return

        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)

    def searchNode(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if root.data > data:
            return self.searchNode(root.left, data)
        else:
            return self.searchNode(root.right, data)

    def findMin(self, root):
      if root is None:
        return
      if root.left:
        return self.findMin(root.left)
      else:
        return root

    def deleteNode(self, root, data):
        if root is None:
            return root

        if root.data > data:
            root.left = self.deleteNode(root.left, data)
        elif root.data < data:
            root.right = self.deleteNode(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

        temp = self.findMin(root.right)
        root.data = temp.data
        root.right = self.deleteNode(root.right, temp.data)

        return root

    def generateTree(self):
        pass


n1 = Node(10)
n2 = Node(5)
n3 = Node(15)

t1 = Tree(n1)
t1.insertNode(t1.root, n2)
t1.insertNode(t1.root, n3)
t1.inOrder(t1.root)
t1.deleteNode(t1.root, 10)
t1.inOrder(t1.root)