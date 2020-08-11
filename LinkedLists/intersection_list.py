"""Given 2 linked list, create a third list with elements present in both these lists"""
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
          while temp.next:
            temp = temp.next
          temp.next = node
        self.count += 1

    def printList(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def generateList(self, num):
        for i in range(num):
            number = random.randint(1, 10)
            temp_node = Node(number)
            self.insertNode(temp_node)

    def sortList(self):
        if not self.head:
            return
        temp = self.head

        while temp.next is not None:
            current = temp
            small = current
            next_node = current.next

            while next_node:
                if next_node.data < small.data:
                    small = next_node
                next_node = next_node.next

            swap_data = small.data
            small.data = current.data
            current.data = swap_data
            temp = temp.next


def intersectionList(l1, l2):
    l = list()
    l3 = LinkedList()
    if l1.count > l2.count:
        first_ptr = l2.head
        second_ptr = l1.head
    else:
        first_ptr = l1.head
        second_ptr = l2.head
    while first_ptr:
        if first_ptr.data not in l:
            l.append(first_ptr.data)
        first_ptr = first_ptr.next
    l.sort()
    while second_ptr:
        if second_ptr.data in l:
          l.remove(second_ptr.data)
          list_node = Node(second_ptr.data)
          l3.insertNode(list_node)
        second_ptr = second_ptr.next
    return l3

l1 = LinkedList()
l1.generateList(15)

l2 = LinkedList()
l2.generateList(17)

l1.printList()
print()
l2.printList()
l3 = intersectionList(l1, l2)
l3.sortList()
print()
l3.printList()


