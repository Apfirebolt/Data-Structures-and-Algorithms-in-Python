
# This is how you define static variables in Python through recursive function calls.


def fun(x):
  print('Inside fun function..', x)
  fun.counter += 1
  print('Counter is now : ', fun.counter)


# This is a static variable
fun.counter = 12
fun(18)