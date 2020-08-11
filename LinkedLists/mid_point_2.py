"""A Program to find the mid point of a linked list using counting method"""
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertNode(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        self.count += 1

    def generateList(self, num):
        for i in range(num):
            temp = random.randint(0, 100)
            temp_node = Node(temp)
            self.insertNode(temp_node)

    def printList(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def midList(self):
        if self.head is None:
            return
        if self.head.next is None:
            return self.head

        temp_count = 0
        temp = self.head
        point = self.count // 2
        while temp:
            temp_count += 1
            temp = temp.next
            if temp_count == point:
                break
        return temp

l1 = LinkedList()
l1.generateList(8)
print()
l1.printList()
print(l1.midList().data)