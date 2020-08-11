"""
Iterators and generators
"""


def generateData():
  for i in range(10):
    yield i

  str_names = ['Amit', 'Indra', 'Pragati']
  for word in str_names:
    yield word


data = generateData()
# data is now a generator on which we can call next() method to get the next value of the iterator
nextItr = next(data)
nextItr2 = next(data)
print('Next iter is : ', nextItr, nextItr2)
for each_data in data:
  print(each_data)