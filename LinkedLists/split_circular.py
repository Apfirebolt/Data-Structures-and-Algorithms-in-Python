"""Given a circular linked list, split it into 2 halves"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular:
    def __init__(self):
        self.head = None

    def insertNode(self, node):
        if self.head is None:
            self.head = node
        if self.head and not self.head.next:
            self.head.next = node
            node.next = self.head
        else:
            temp = self.head.next
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head

    def printList(self):
        if self.head is None:
            return -1
        if self.head and not self.head.next:
            return self.head.data

        temp = self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp.next == self.head:
                print(temp.data, end=' ')
                break


    def splitHalves(self):
            # Initialize the head pointers of both the linked lists
            self.first = None
            self.second = None
            slow = self.head
            fast = self.head

            while True:
                slow = slow.next
                fast = fast.next.next

                if fast is self.head or fast.next == self.head:
                    break
            temp = self.head
            self.first = temp
            while temp != slow:
                print('Slow : ', temp.data)
                temp = temp.next

    def deleteNodes(self):
        if self.head is None:
            return -1
        current = self.head
        while current:
            next = current.next  # move next node
            del current.data
            current = next

n1 = Node(16)
n2 = Node(12)
n3 = Node(5)
n4 = Node(7)
n5 = Node(18)
n6 = Node(9)
c = Circular()
c.insertNode(n1)
c.insertNode(n2)
c.insertNode(n3)
c.insertNode(n4)
c.insertNode(n5)
c.insertNode(n6)
c.printList()
c.splitHalves()
c.printList()
