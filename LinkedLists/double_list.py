""" Program to code a double linked list with n random elements """

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, node):
        if not self.head:
            self.head = node

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.previous = temp
            self.tail = node

    def displayList(self):
        if not self.head:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def generateRandom(self, num):
        for i in range(num):
            number = random.randint(0, 100)
            temp_node = Node(number)
            self.insertNode(temp_node)

    def printReverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=' ')
            temp = temp.previous


l1 = LinkedList()
l1.generateRandom(12)
l1.displayList()
print('')
l1.printReverse()