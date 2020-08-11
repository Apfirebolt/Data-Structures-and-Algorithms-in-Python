"""A program to perform sorting on linked list"""
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def nextNode(self):
        return self.next

    def displayData(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, node):
        if self.head is None:
          self.head = node
        else:
          temp = self.head
          while temp.next is not None:
            temp = temp.next
          temp.next = node

    def generateList(self, num):
        for i in range(num):
            temp = random.randint(0, 100)
            temp_node = Node(temp)
            self.insertNode(temp_node)

    def displayList(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def sortList(self):
        if self.head is None:
            return

        current_node = self.head
        while current_node:
            smallest = current_node
            itr = current_node.next

            while itr:
                if itr.data < smallest.data:
                    smallest = itr
                itr = itr.next
            # Swap values using a variable
            temp = smallest.data
            smallest.data = current_node.data
            current_node.data = temp
            current_node = current_node.next

l1 = LinkedList()
l1.generateList(13)
l1.displayList()
l1.sortList()
print('')
l1.displayList()