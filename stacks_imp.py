import random


class Stacks:
    def __init__(self, size):
        self.size = size
        self.stack_list = [0] * size
        self.top = -1

    def pushElement(self, ele):
        if len(self.stack_list) >= self.size:
            self.top += 1
            self.stack_list.insert(0, ele)
            del self.stack_list[len(self.stack_list)-1]
        else:
            raise ValueError('Stack is full')

    def popElement(self):
        if not len(self.stack_list):
            raise ValueError('No element to pop, empty stack!')
        else:
            ele = self.stack_list[self.top]
            del self.stack_list[self.top]
            self.top -= 1
            return ele

    def pushRandomElements(self):
        for i in range (self.size):
            temp_num = random.randint(0, 100)
            self.pushElement(temp_num)

    @property
    def printStack(self):
        return self.stack_list


s1 = Stacks(8)
s1.pushRandomElements()
s1.pushElement(10)
s1.pushElement(6)
s1.pushElement(8)
# print(s1.printStack())
# print(s1.popElement())
print(s1.printStack)
# print(s1.top)