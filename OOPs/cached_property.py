"""
This would deal with property and cached property decorators of python
"""


class Sample:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @property
  def printX(self):
    return self.x


  def printY(self):
    return self.y


obj1 = Sample(12, 20)
# This can be accessed as data even though it is a method
print(obj1.printX)
print(obj1.printY())