from collections import namedtuple

Student1 = namedtuple('Student',['name','age','DOB'])
Student2 = namedtuple('Student', ['name', 'age', 'DOB'])

S1 = Student1('Nandini','19','2541997')
S2 = Student2('Shashank', '21', '674539')

l2 = ['Dwayne', '25', '7856490']

for i in S1:
    print(i)
print(S1._fields)
# Printing the name and age attributes
print(S1.name, S1.age)
S1 = S1._make(l2)
S1 = S1._replace(name = 'Manjeet')
print('After modification', S1.name, S1.age)

for i in S2:
    print(i)
print(S2._fields)
# Printing as dictionary
print(S2._asdict())



