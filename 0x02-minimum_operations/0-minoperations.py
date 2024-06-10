#!/usr/bin/python3
"""
Minimum Operations
Given num n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file
Prototype: def minOperations(n)
Returns an integer
if n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    Function
    Returns an integer
    """
    res = 0
    a = 2
    while n > 1:
        while n % a == 0:
            res += a
            n /= a
        a += 1
    return res
