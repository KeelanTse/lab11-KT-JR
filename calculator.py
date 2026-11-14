"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

import math

def add(a, b): a + b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b): b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b): loga(b)# use math library/raise ValueError

def exponent(a, b): a^b

"""
<<<<<<< HEAD
=======
# First example
>>>>>>> a0327771d0a3c329d4d52bf33adbc44ce0973960
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("Input must be a number")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Inputs must be numbers")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b