"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(num1, num2):
    return num1 * num2

def id(smth):
    return smth

def add(num1, num2):
    return num1 + num2

def neg(num):
    return -num

def lt(num1, num2):
    return num1 < num2

def eq(num1, num2):
    return num1 == num2

def max(num1, num2):
    return num1 if num1 > num2 else num2

def is_close(num1, num2):
    return abs(num1 - num2) < 1e-2

def sigmoid(num):
    return 1.0 / (1.0 + exp(-num)) if num >= 0 else exp(num) / (1.0 + exp(num))

def relu(num):
    return max(0, num)

def log(num):
    return math.log(num)

def exp(num):
    return math.exp(num)

def inv(num):
    return 1.0 / num

def log_back(num1, num2):
    return (1.0 / num1) * num2

def inv_back(num1, num2):
    return (-1.0 / (num1 * num1)) * num2

def relu_back(num1, num2):
    return num2 if num1 > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(func: Callable, items: Iterable):
    return [func(item) for item in items]

def zipWith(func: Callable, items1: Iterable, items2: Iterable):
    return [func(item1, item2) for item1, item2, in zip(items1, items2)]

def reduce(func: Callable, items: Iterable):
    result = None
    for item in items:
        if result is None:
            result = item
        else:
            result = func(result, item)
    return result or 0

def negList(items: Iterable):
    return map(neg, items)

def addLists(items1: Iterable, items2: Iterable):
    return zipWith(add, items1, items2)

def sum(items: Iterable):
    return reduce(add, items)

def prod(items: Iterable):
    return reduce(mul, items)
