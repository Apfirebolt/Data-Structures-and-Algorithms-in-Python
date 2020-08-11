"""
Class attributes
"""


class People:
  people_count = 100
  total_cnt = 10

  def __init__(self):
    pass


class Person(People):
  person_count = 0

  def __init__(self, username):
    self.username = username
    Person.person_count += 1  # here is how you access class variables
    People.people_count += 1

    # Note that you don't need to pass self when cls is passed

  def classVars(cls):
    print('Class variable passed..', cls.person_count)


ashley = Person("Ashley")
ashley.home_work = True
print('Ashley home work, ', ashley.home_work)

# Existence of an attribute for specific objects, must be passed as string
if hasattr(ashley, 'home_work'):
  print('Yes, Ashley done the homework')
else:
  print('No does not exist')
daphne = Person("Daffy")

# Calling class level method
ashley.classVars()
print(Person.person_count)
print(Person.people_count)