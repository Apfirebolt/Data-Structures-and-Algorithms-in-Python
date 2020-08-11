"""
Class level variables defined
"""

# Class level decorators


def classDecorator(fun):
  def inner(a):
    b = 18
    fun(a, b)
    print('Inside the inner method...', a, b)
  return inner


@classDecorator
class Sample:
  def __init__(self, a, b):
    self.a = a
    self.b = b
    print('Sample initialized...')

  def anotherFun(self):
    print('Inside another fun..')

s1 = Sample(10)
