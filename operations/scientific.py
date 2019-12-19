import math


def factorial(n):
    """
    author:junior
    n: integer
    """
    if type(n) == int:
        if n > 1:
            return n*factorial(n-1)
        else:
            return 1
    else:
        print('not integer')


def exponential(n):
    pass


def logarithm(x, base):
    """
    Return the logarithm of x to the given base.
    """
    return math.log(x, base)
