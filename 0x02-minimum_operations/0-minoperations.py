#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Function minOperations
    """
    r = 0
    y = 2
    while n > 1:
        while n % y == 0:
            r += y
            n /= y
        y += 1
    return r
