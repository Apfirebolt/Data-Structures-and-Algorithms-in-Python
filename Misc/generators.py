# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    yield n

    n += 1
    yield n
    yield 102

custom = my_gen()

for i in custom:
    print(i)