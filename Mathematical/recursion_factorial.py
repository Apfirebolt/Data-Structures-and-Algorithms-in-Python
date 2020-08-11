""" Find the factorial of a given number < 20 through recursion """

def findFactorial(n):
    if n == 1:
        return 1
    else:
        return n * findFactorial(n-1)

try:
    n = int(input())
    if n > 20:
        raise ValueError("The number cannot be greater than 20")
    print(findFactorial(n))
except ValueError as Err:
    print(Err)