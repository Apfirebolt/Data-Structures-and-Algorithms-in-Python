"""A Program to demonstrate class and static methods in Python"""


class Nero:
    numbers = [12, 18, 17, 21, 6]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def printName(self):
        return self.name

    @classmethod
    def printNumbers(cls):
        return cls.numbers

    @classmethod
    def createInstance(cls, name, age):
        return cls(name, age)


n1 = Nero('Anit', 17)
# Creating an object instance using class method.
n2 = Nero.createInstance('Pragati', 27)

print(n2.name)
print(n1.printName)
print(n1.numbers)
print(Nero.printNumbers())
