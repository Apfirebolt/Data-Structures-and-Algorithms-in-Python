"""Program for basic operations on a single linked list"""

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

    def insertAtBegin(self, node):
        node.next = self.head
        self.head = node

    def searchNode(self, data):
        if self.head is None:
            return
        temp = self.head
        while temp.next is not None:
            if temp.data == data:
                return data
            temp = temp.next
        return -1

    def deleteNode(self, data):
        if self.head is None:
            return
        # If data to be deleted is present at head
        if self.head.data == data:
            deleteNode = self.head
            self.head = deleteNode.next
            del deleteNode

        temp = self.head
        while temp and temp.next is not None:
            if temp.next.data == data:
                deleteNode = temp.next
                temp.next = deleteNode.next
                del deleteNode
            temp = temp.next

    def displayList(self):
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def countNodes(self):
        if self.head is None:
            return
        cnt = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            cnt += 1
        return cnt

    def reverseList(self):
        if self.head is None:
            return

        current_node = self.head
        next_node = None
        prev_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node


n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(12)

l1 = LinkedList()
l1.insertNode(n1)
l1.insertNode(n2)
l1.insertNode(n3)
l1.insertAtBegin(n4)
l1.displayList()
# print('Total Nodes : ', l1.countNodes())
# print('Searched data : ', l1.searchNode(7))
# l1.deleteNode(7)
l1.reverseList()
l1.displayList()