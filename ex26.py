# -*- coding: utf-8 -*-
import nltk
from timeit import Timer

def catalan_r(n):
    """
    Return Catalan number with recursion method.
    Type of n is int.
    """
    assert isinstance(n, int),"Please input int parameter."
    if n < 0:
        return 0
    elif n == 0:
        return 1

    return sum( catalan_r(i) * catalan_r(n-1-i) for i in range(n))

def catalan_d(n, lookup = {0:1}):
    """
    Return Catalan number with dynamic method.
    Type of n is int.
    """
    assert isinstance(n, int),"Please input int parameter."
    if n < 0:
        return 0
    if n not in lookup:
        lookup[n] = sum(catalan_d(i, lookup) * catalan_d(n-1-i, lookup)
                        for i in range(n))
    return lookup[n]

print(Timer("catalan_r(15)", "from ex26 import catalan_r").timeit(1))
print(Timer("catalan_d(15)", "from ex26 import catalan_d").timeit(1))
