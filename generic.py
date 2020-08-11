class Alpha(object):
    def __init__(self, number, name):
        self.num = number
        self.name = name
        self.n = 2
        self.max = 3

    def __call__(self, *args, **kwargs):
        print('Calling constructor..', args, kwargs)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= 10:
            result = 2 + self.n
            self.n += 1
            return result
        else:
            raise StopIteration

    def __repr__(self):
        return 'Repr({!r}, {!r})'.format(self.num, self.name)

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.num + other

    def __mul__(self, other):
        return self.num * other

    def __sub__(self, other):
        return self.num - other

    def __divmod__(self, other):
        return self.num % other

    # You can apply len(object) if you've used this magic method
    def __len__(self):
        return 21

    def printNum(self):
        return self.num


class Beta(Alpha):

    def childCall(self):
        print(super().printNum())
        # print(super(Beta, self).printNum())


b = Beta(13, 'Dave')
b.childCall()
print('Length of an object : ', len(b))
# Object call
b('Daisy', 15, [1, 6, 12, 19], amit=15, rosh=18)

# String representation of object
print(b)

# Repr formatted string representation of the object
print(repr(b))

# Adding of object, value of other is 60
print(b + 60)

# Subtraction of object, value of other is 2
print(b - 2)

# Multiplication of object, value of other is 4
print(b * 4)


# Iterables from object
i = iter(b)
for each_itr in i:
    print('Each iterator is : ', each_itr)

# Access all properties of an object
print(b.__dict__)