class Sample():
    # Magic/Dunder methods
    

    def setPrivate(self, post):
        self.__post = post

    def displayPost(self):
        return self.__post

    def displayName(self):
        pass

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized..')

    def __call__(self, *args, **kwargs):
        print('Inside call method..', args, kwargs)

s1 = Sample('Amit', 27)
s2 = Sample('Pragati', 26)

print(s1.name)
print(s2.name)
s1.setPrivate('Manager')
# print(s1.__post)
print(s1.displayPost())
print(type(int))
print(type(s1))

s1(1, 4, 11, amit=16, alka=60)
print('S1 ', s1)