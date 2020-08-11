"""Given a binary tree, print the level which has max sum and also the sum of nodes at this level"""

import random
import sys

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
        q.append(self.root)

        while len(q):
            temp = q.pop(0)
            print(temp.data, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    def maxLevelSum(self):
      q = [self.root, None]
      global_max = -1
      current_sum = 0
      level = 1
      max_level = -1
      while len(q):
        current_node = q.pop(0)
        # Level change
        if current_node is None:
          if len(q):
            if current_sum > global_max:
              global_max = current_sum
              max_level = level
            current_sum = 0
            level += 1
            q.append(None)
        else:
          current_sum += current_node.data
          if current_node.left:
            q.append(current_node.left)
          if current_node.right:
            q.append(current_node.right)

      if global_max > current_sum:
        return max_level, global_max
      else:
        return max_level + 1, current_sum


def generateTree(arr):
    n1 = Node(arr[0])
    t1 = TreeNode(n1)

    for i in range(1, len(arr)):
        t1.insert_node(arr[i])
    return t1

arr = [1, 12, 4, 12, 18, 21, 7, 2, 7, 1, 9, 5, 3, 10, 12]
t1 = generateTree(arr)
t1.levelOrder()
print('\n', t1.maxLevelSum())