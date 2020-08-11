class Home(object):
    def __init__(self, marks):
        self.marks = marks

    # Rank is a private variable, declared using double underscores
    def set_rank(self, rank):
        self.__rank = rank

    # Method written to retrive private variable value
    def get_rank(self):
        return self.__rank


h1 = Home([1, 7, 12])
h2 = Home([5, 9, 18])
print(h1.marks)
h1.set_rank(9)

# This won't work
# print(h1.__rank)

# This works
print(h1.get_rank())

# Now defining custom properties in a class using setAttr, age is not defined in class definition but you can still set it
setattr(h1, 'age', 40)
print(h1.age)

# Check if a given object has a property or not, this returns True
if hasattr(h1, 'age'):
    print('H1 does have age attribute')
else:
    print('No age attribute')

# HasAttr here returns false
if hasattr(h2, 'age'):
    print('H2 does have marks')
else:
    print('NO marks in H2')

# Getting attribute using 'getattr'
print(getattr(h2, 'marks'))