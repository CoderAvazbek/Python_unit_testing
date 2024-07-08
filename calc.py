def add(a, b):
    """ Add Function """
    return a + b


def subtract(a, b):
    """ Subtract Function """
    return a - b


def multiply(a, b):
    """ Multiply Function """
    return a * b


def divide(a, b):
    """ Divide Function """
    if b == 0:
        raise ValueError("Can not divide by zero")
    return a / b
