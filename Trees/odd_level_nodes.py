"""Given a Binary Tree, print all the nodes which are at odd levels starting from top - bottom"""

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


    def levelOrder(self):
        q = []
        level = 1
        q.append(self.root)
        q.append(None)
        while len(q):
            temp_node = q.pop(0)
            if temp_node is None:
                level += 1
                if len(q):
                    q.append(None)
                else:
                    break
            else:
                if level % 2:
                    print(temp_node.data, end=' ')
                if temp_node.left:
                  q.append(temp_node.left)
                if temp_node.right:
                  q.append(temp_node.right)

n1 = Node(1)
t1 = TreeNode(n1)
for i in range(2, 20):
    t1.insert_node(i)
t1.levelOrder()
