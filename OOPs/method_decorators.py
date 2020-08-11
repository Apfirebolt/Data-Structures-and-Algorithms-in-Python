"""
Decorators for classes - Practical application, access the variables of inner function, modify them and return through outer
functions.
"""

# Example 1
def classDecorator(fun):
  def inner(*args, **kwargs):
    args_length = fun(*args, **kwargs)
    args_length += 10
    print('Inside the inner function..', args, kwargs)
    print('Now the argument length is : ', args_length)
  return inner


@classDecorator
def decorateMe(*args, **kwargs):
  print('I would be decorated..', args, kwargs)
  return len(args)

decorateMe(10, 6, 'Amit', Pragati=12, Alka=18)


# Example 2, x is passed to the inner function defined inside the decorator
def methodDecorator(foo):
  def inner(x):
    x = foo(x)
    print('X : ', x)
    return x
  return inner


@methodDecorator
def bar(x):
  print('X inside bar is : ', x)
  return x + 7

print(bar(10))