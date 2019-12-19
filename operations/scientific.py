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


def logarithm(n, m):
    pass
