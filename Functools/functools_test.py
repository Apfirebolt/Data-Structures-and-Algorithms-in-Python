import functools


def randomFun():
  print('A random function..')


def somethingMore(fun):
  fun()
  print('Something more called..')

somethingMore(randomFun)