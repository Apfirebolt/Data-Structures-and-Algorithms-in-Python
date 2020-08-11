import random

class Stack:
    def __init__(self):
        self.stack_list = []

    def pushElement(self, ele):
        self.stack_list.insert(0, ele)

    def popElement(self):
        return self.stack_list.pop(0)

    def insertRandom(self, num):
        for i in range(num):
            temp_num = random.randint(1, 200)
            self.pushElement(temp_num)

    @property
    def displayStack(self):
        return self.stack_list


s1 = Stack()
s1.insertRandom(7)
print(s1.displayStack)
print(s1.popElement())
print(s1.displayStack)