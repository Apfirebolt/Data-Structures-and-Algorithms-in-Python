"""A program to implement stacks using linked list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackList:
    def __init__(self):
        self.head = None
        self.count = 0

    def pushElement(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def popElement(self):
        if self.head is None:
            return -1
        data = self.head.data
        temp_node = self.head
        self.head = temp_node.next
        temp_node = None
        return data

    def peekElement(self):
        if self.head is None:
            return -1
        else:
            return self.head.data

    def printStack(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

n1 = Node(7)
n2 = Node(12)
n3 = Node(4)
n4 = Node(6)
n5 = Node(3)

s1 = StackList()
s1.pushElement(n1)
s1.pushElement(n2)
s1.pushElement(n3)
s1.pushElement(n4)

s1.printStack()
print(s1.popElement())
print(s1.popElement())
s1.printStack()
s1.pushElement(n5)
print('After popping!')
s1.printStack()
print('Top element : ', s1.peekElement())
