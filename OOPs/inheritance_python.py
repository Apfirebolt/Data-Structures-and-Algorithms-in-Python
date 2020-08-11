"""
Inheritance in Python explained with examples
"""


class Father:
  def __init__(self, f):
    self.f = f
    print('Father class')

  def fun(self):
    print('Inside the father fun method..')


class Mother:
  def __init__(self, m):
    self.m = m
    print('Mother class')

  # If we comment out the fun method in the class then this fun method would be called next
  def fun(self):
    print('Inside the mother fun method...')


# Inheritance orders from right to left, Mother's constructor would be called, explicitly calling father's constructor.
class Child(Mother, Father):
  def __init__(self, c, m, f):
    super(Child, self).__init__(m)
    Father.__init__(self, f)
    self.c = c
    print('Child class')

  # This method would be called by default in case method names are similar
  def fun(self):
    print('Inside the child fun method')

  def anotherFun(self):
    # Calling fun method of self, Mother class and the Father class, self must be passed to the father class method
    self.fun()
    super(Child, self).fun()
    Father.fun(self)

c1 = Child(12, 8, 10)
print(c1.c, c1.m, c1.f)
c1.fun()
c1.anotherFun()
