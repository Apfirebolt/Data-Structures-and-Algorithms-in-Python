"""Binary Tree operations"""

from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert_node(self, data):
        new_node = TreeNode(data)
        d = deque()
        d.append(self.root)

        while len(d):
            # If full node, then simply pop it.
            temp_node = d.popleft()
            if temp_node.left is None:
                temp_node.left = new_node
                break
            else:
                d.append(temp_node.left)
            if temp_node.right is None:
                temp_node.right = new_node
                break
            else:
                d.append(temp_node.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=' ')
        self.inOrder(root.right)

    def levelOrder(self):
        d = deque()
        d.append(self.root)

        while len(d):
            temp_node = d.popleft()
            print(temp_node.data, end=' ')
            if temp_node.left:
                d.append(temp_node.left)
            if temp_node.right:
                d.append(temp_node.right)

n1 = TreeNode(5)
b1 = BinaryTree(n1)
b1.insert_node(7)
b1.insert_node(12)
b1.insert_node(18)
b1.insert_node(21)
b1.insert_node(2)
b1.insert_node(17)
b1.inOrder(b1.root)
print()
b1.inOrder(b1.root)




